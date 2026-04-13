#!/usr/bin/env bash
set -e

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
BUCKET="gs://gabonese-corpus/processed"
OUTPUT_DIR="$BASE_DIR/output"

if [ -d "$OUTPUT_DIR" ]; then
  echo "Sync $OUTPUT_DIR → $BUCKET"
  gcloud storage rsync "$OUTPUT_DIR" "$BUCKET" --recursive
else
  echo "❌ dossier $OUTPUT_DIR introuvable"
  exit 1
fi

echo "✅ PROCESSED synchronisé"