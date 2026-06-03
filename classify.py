import os
import pdfplumber
import pandas as pd
import joblib

from nlp_utils import clean_text
from summarizer import generate_summary

PDF_FOLDER = "taskpdf"

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

results = []

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(PDF_FOLDER, file)

        text = ""

        try:

            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text

            cleaned_text = clean_text(text)

            X_test = vectorizer.transform([cleaned_text])

            category = model.predict(X_test)[0]

            confidence = max(
                model.predict_proba(X_test)[0]
            ) * 100

            summary = generate_summary(text)

            print("\n" + "=" * 60)
            print(f"FILE: {file}")
            print("=" * 60)

            print(f"Category: {category}")
            print(f"Confidence: {confidence:.2f}%")
            print(f"Summary: {summary}")

            results.append({
                "filename": file,
                "category": category,
                "confidence": round(confidence, 2),
                "summary": summary
            })

        except Exception as e:

            print(f"Error processing {file}: {e}")

df = pd.DataFrame(results)

df.to_csv("results.csv", index=False)

print("\nresults.csv generated successfully!")