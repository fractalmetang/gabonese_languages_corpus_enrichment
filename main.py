
import argparse


def invert_file(input_path: str, output_path: str):
    total = 0
    kept = 0
    skipped = 0

    with open(input_path, "r", encoding="utf-8") as fin, \
         open(output_path, "w", encoding="utf-8") as fout:

        for i, line in enumerate(fin, start=1):
            total += 1
            line = line.rstrip("\n")

            if not line.strip():
                skipped += 1
                continue

            # split sur 4 espaces
            parts = line.split("    ")

            if len(parts) != 2:
                print(f"[WARN] Ligne {i} invalide: {line}")
                skipped += 1
                continue

            src, tgt = parts  # src = lang_cible, tgt = fr

            if not src.strip() or not tgt.strip():
                skipped += 1
                continue

            # inversion + conversion propre en TAB (recommandé)
            fout.write(f"{tgt.strip()}    {src.strip()}\n")
            kept += 1

    print("----- Résumé -----")
    print(f"Total lignes   : {total}")
    print(f"Lignes gardées : {kept}")
    print(f"Lignes ignorées: {skipped}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    invert_file(args.input, args.output)