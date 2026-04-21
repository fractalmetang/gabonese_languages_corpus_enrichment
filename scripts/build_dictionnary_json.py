import json
from pathlib import Path

LANGS = ["douma", "nzebi", "fang", "obamba", "omyènè", "punu", "tshogo"]

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def process_language(lang):
    BASE_DIR = Path(__file__).resolve().parent.parent
    lang_dir = BASE_DIR / lang
    files = list(lang_dir.rglob("*.txt"))
    entries = []

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split("    ")  # 4 espaces

                if len(parts) >= 2:
                    source = parts[0].strip()
                    target = parts[1].strip()

                entries.append({
                    "word": source,
                    "translation": target,
                    "lang": lang
                })

    output_file = OUTPUT_DIR / f"{lang}_dictionary.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"✅ {lang} → {output_file} ({len(entries)} entrées)")


def main():
    for lang in LANGS:
        BASE_DIR = Path(__file__).resolve().parent.parent
        lang_path = BASE_DIR / lang
        if lang_path.exists():
            
            process_language(lang)


if __name__ == "__main__":
    main()
