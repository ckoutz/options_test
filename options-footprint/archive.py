"""
Archive a big table out of the database to a compressed file, and restore it if ever needed.

Used for ladder_trades (the million hypothetical option trades from the ladder backtest): the
summary lives on in ladder_report and the agents' candidate sample is already built, so the raw
trades can move out of Neon to a GitHub Release and free most of the free-plan storage.

    python archive.py export --table ladder_trades --out ladder_trades.csv.gz
    python archive.py drop   --table ladder_trades --manifest ladder_trades.manifest.json
    python archive.py restore --table ladder_trades --file ladder_trades.csv.gz

`drop` refuses unless the table still has exactly the row count recorded in the manifest and the
manifest says the upload was verified, so nothing is deleted on a half-finished archive.
"""
import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import sys

import psycopg

ALLOWED = {"ladder_trades"}


def connect():
    url = os.environ.get("DATABASE_URL")
    if not url:
        sys.exit("Set DATABASE_URL first.")
    return psycopg.connect(url, autocommit=True)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def export(a):
    if a.table not in ALLOWED:
        sys.exit(f"Only {sorted(ALLOWED)} can be archived.")
    conn = connect()
    rows_db = conn.execute(f"select count(*) from {a.table}").fetchone()[0]
    with gzip.open(a.out, "wb", compresslevel=9) as gz, conn.cursor() as cur:
        with cur.copy(f"COPY {a.table} TO STDOUT WITH (FORMAT csv, HEADER true)") as copy:
            for data in copy:
                gz.write(data)
    # Read the file back and count rows with a real CSV parser (fields may contain newlines).
    with gzip.open(a.out, "rt", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows_file = sum(1 for _ in reader)
    if rows_file != rows_db:
        sys.exit(f"Row count mismatch: database {rows_db:,}, file {rows_file:,}. Not safe to continue.")
    manifest = {"table": a.table, "rows": rows_db, "columns": header, "file": os.path.basename(a.out),
                "bytes": os.path.getsize(a.out), "sha256": sha256(a.out), "upload_verified": False}
    with open(a.manifest, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Exported {rows_db:,} rows of {a.table} to {a.out} ({manifest['bytes'] / 1e6:.1f} MB), verified.")


def mark_uploaded(a):
    m = json.load(open(a.manifest))
    if a.asset_bytes != m["bytes"]:
        sys.exit(f"Uploaded size {a.asset_bytes} does not match the file ({m['bytes']}). Not marking verified.")
    m["upload_verified"] = True
    m["release"] = a.release
    json.dump(m, open(a.manifest, "w"), indent=2)
    print(f"Upload verified: {a.release} ({a.asset_bytes:,} bytes).")


def drop(a):
    m = json.load(open(a.manifest))
    if m.get("table") != a.table or a.table not in ALLOWED:
        sys.exit("Manifest does not match this table.")
    if not m.get("upload_verified"):
        sys.exit("The archive upload was not verified; refusing to drop anything.")
    conn = connect()
    rows_now = conn.execute(f"select count(*) from {a.table}").fetchone()[0]
    if rows_now != m["rows"]:
        sys.exit(f"Table now has {rows_now:,} rows but the archive has {m['rows']:,}; refusing to drop.")
    before = conn.execute("select pg_database_size(current_database())").fetchone()[0]
    conn.execute(f"drop table {a.table}")
    after = conn.execute("select pg_database_size(current_database())").fetchone()[0]
    print(f"Dropped {a.table} ({m['rows']:,} rows). Database size {before / 1e6:.0f} MB -> {after / 1e6:.0f} MB.")
    print(f"Restore any time with: python archive.py restore --table {a.table} --file {m['file']} "
          f"(download it from release {m.get('release')}).")


def restore(a):
    if a.table not in ALLOWED:
        sys.exit(f"Only {sorted(ALLOWED)} can be restored.")
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from store import Store   # creates the table (empty) if it doesn't exist
    Store()
    conn = connect()
    if conn.execute(f"select count(*) from {a.table}").fetchone()[0]:
        sys.exit(f"{a.table} is not empty; refusing to restore on top of existing rows.")
    with gzip.open(a.file, "rt", newline="") as f:
        header = next(csv.reader(io.StringIO(f.readline())))
    cols = ", ".join(header)
    with gzip.open(a.file, "rb") as gz, conn.cursor() as cur:
        with cur.copy(f"COPY {a.table} ({cols}) FROM STDIN WITH (FORMAT csv, HEADER true)") as copy:
            for chunk in iter(lambda: gz.read(1 << 20), b""):
                copy.write(chunk)
    n = conn.execute(f"select count(*) from {a.table}").fetchone()[0]
    print(f"Restored {n:,} rows into {a.table}.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export"); e.add_argument("--table", required=True); e.add_argument("--out", required=True)
    e.add_argument("--manifest", required=True)
    u = sub.add_parser("mark-uploaded"); u.add_argument("--manifest", required=True)
    u.add_argument("--asset-bytes", type=int, required=True); u.add_argument("--release", required=True)
    d = sub.add_parser("drop"); d.add_argument("--table", required=True); d.add_argument("--manifest", required=True)
    r = sub.add_parser("restore"); r.add_argument("--table", required=True); r.add_argument("--file", required=True)
    a = p.parse_args()
    {"export": export, "mark-uploaded": mark_uploaded, "drop": drop, "restore": restore}[a.cmd](a)


if __name__ == "__main__":
    main()
