#!/usr/bin/env python3
"""Compare table row counts from two CSV exports: table,count"""
from __future__ import annotations
import argparse, csv, sys

def load(path):
    d = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            d[row["table"]] = int(row["count"])
    return d

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--target", required=True)
    p.add_argument("--tolerance", type=int, default=0)
    args = p.parse_args()
    s, t = load(args.source), load(args.target)
    tables = sorted(set(s) | set(t))
    bad = 0
    for table in tables:
        sc, tc = s.get(table), t.get(table)
        if sc is None or tc is None:
            print(f"MISSING  {table}  source={sc} target={tc}")
            bad += 1
            continue
        diff = abs(sc - tc)
        status = "OK" if diff <= args.tolerance else "DRIFT"
        if status != "OK":
            bad += 1
        print(f"{status:5}  {table}  source={sc} target={tc} diff={diff}")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
