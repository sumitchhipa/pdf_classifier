import os
import pdfplumber
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from nlp_utils import clean_text

PDF_FOLDER = "taskpdf"

texts = []
labels = []

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

            texts.append(cleaned_text)

            filename = file.lower()

            if "contract" in filename:
                labels.append("Contract")

            elif "invoice" in filename:
                labels.append("Invoice")

            elif "report" in filename:
                labels.append("Report")

            elif "resume" in filename:
                labels.append("Resume")

            else:
                labels.append("Unknown")

        except Exception as e:

            print(f"Error reading {file}: {e}")

print(f"Total Documents: {len(texts)}")
print(f"Labels: {labels}")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

model = MultinomialNB()

model.fit(X, labels)

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel trained successfully!")
print("model.pkl saved")
print("vectorizer.pkl saved")