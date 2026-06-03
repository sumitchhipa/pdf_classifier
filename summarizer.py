def generate_summary(text):

    text = text.replace("\n", " ")

    sentences = text.split(".")

    summary = ". ".join(sentences[:2])

    return summary.strip()