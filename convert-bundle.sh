#!/bin/bash
set -euo pipefail

curl -o lab3.tar.gz https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

tar -xzf lab3.tar.gz

# awk can remove blank / whitespace-only lines
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

row_count=$(($(wc -l < cleaned.csv) - 1))
echo "row count: $row_count"

tar -czf converted-archive.tar.gz cleaned.csv
