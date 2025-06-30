#!/bin/bash
set -e

docs_dir=${1:-docs/diagrams}
output_dir=${2:-docs/generated}

mkdir -p "$output_dir"

# Render PlantUML diagrams
find "$docs_dir" -name '*.puml' -print0 | while IFS= read -r -d '' file; do
  plantuml -tpng "$file" -o "$PWD/$output_dir"
done

# Render Mermaid diagrams
find "$docs_dir" -name '*.mmd' -print0 | while IFS= read -r -d '' file; do
  base=$(basename "$file" .mmd)
  mmdc -i "$file" -o "$output_dir/${base}.png" \
    --puppeteerConfigFile "$(dirname "$0")/puppeteer.json"
done

echo "Diagrams generated in $output_dir"
