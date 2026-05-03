#!/usr/bin/env bash
set -e

BUCKET="gs://gabonese-corpus/raw"

LANGS=("douma" "fang" "nzebi" "obamba" "omyènè" "punu" "tshogo" "toli_bagando")

for lang in "${LANGS[@]}"; do
  echo "Sync $lang → $BUCKET/$lang"
  gcloud storage rsync "$lang" "$BUCKET/$lang" --recursive
done

echo "✅ Synchronisation terminée"