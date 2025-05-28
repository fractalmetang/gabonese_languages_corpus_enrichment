from PIL import Image
import pdfplumber
import re

import pytesseract
import pdf2image


# pages = pdf2image.convert_from_path("adouma_from_dahin.pdf")
# for page in pages:
#     text = pytesseract.image_to_string(page)
#     print(text)

# Ouvre le fichier PDF
with pdfplumber.open("adouma_from_dahin.pdf") as pdf:
    extracted_pairs = []

    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue

        # Nettoyage de la page
        lines = text.split("\n")
        for line in lines:
            # Tente de détecter un format : "Mot français ... Traduction"
            match = re.match(r"^([A-ZÉÈÀÇa-zéèàùûçîôî'’\- ]+)\s+([A-Za-z, \-'.àéèêôûîâïüöç]+)$", line)
            if match:
                french = match.group(1).strip()
                adouma = match.group(2).strip()
                extracted_pairs.append((french, adouma))

print(extracted_pairs)
