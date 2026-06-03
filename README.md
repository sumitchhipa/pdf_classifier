# PDF Document Classification using NLP

A Python-based NLP project that automatically classifies PDF documents into predefined categories and generates a short summary for each document.

## Features

* PDF text extraction using pdfplumber
* NLP preprocessing

  * Lowercase conversion
  * Punctuation removal
  * Stopword removal
* TF-IDF vectorization
* Document classification using Multinomial Naive Bayes
* Confidence score generation
* Automatic summary generation
* CSV output export

## Project Workflow

PDF Document

↓

Text Extraction

↓

Text Preprocessing

↓

TF-IDF Vectorization

↓

Multinomial Naive Bayes Classification

↓

Confidence Score

↓

Summary Generation

↓

CSV Output

## Technologies Used

* Python
* pdfplumber
* NLTK
* Scikit-learn
* Pandas
* Joblib

## Project Structure

```text
pdfclassify/
│
├── taskpdf/
│   ├── contract_realistic.pdf
│   ├── invoice_realistic.pdf
│   ├── report_realistic.pdf
│   └── resume_realistic.pdf
│
├── classify.py
├── train_model.py
├── nlp_utils.py
├── summarizer.py
│
├── model.pkl
├── vectorizer.pkl
│
├── results.csv
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd pdfclassify
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Train Model

```bash
python train_model.py
```

## Run Classification

```bash
python classify.py
```

## Output

The script generates:

* Predicted document category
* Confidence score
* Short document summary
* results.csv file

## Example Categories

* Contract
* Invoice
* Report
* Resume

## Future Improvements

* Larger training dataset
* Advanced summarization
* BERT-based classification
* Web interface using Streamlit
* Multi-category document support

## Author

Sumit Chhipa
MCA Student | Data Science & Machine Learning Enthusiast
