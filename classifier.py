def classify_document(text):

    text = text.lower()

    categories = {
        "Contract": [
            "agreement",
            "confidentiality",
            "termination",
            "governing law"
        ],

        "Invoice": [
            "invoice",
            "vendor",
            "gst",
            "subtotal",
            "payment"
        ],

        "Report": [
            "executive summary",
            "analysis",
            "revenue",
            "recommendations"
        ],

        "Resume": [
            "skills",
            "education",
            "internship",
            "certifications",
            "curriculum vitae"
        ]
    }

    scores = {}

    for category, keywords in categories.items():

        score = 0

        for keyword in keywords:

            if keyword in text:
                score += 1

        scores[category] = score

    best_category = max(scores, key=scores.get)

    total = sum(scores.values())

    confidence = (
        scores[best_category] / total
        if total > 0 else 0
    )

    return best_category, round(confidence * 100, 2)