
import os
from pypdf import PdfReader


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file.
    """

    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_txt(file_path):
    """
    Extract text from a TXT file.
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def extract_text(file_path):
    """
    Automatically detect file type
    and extract its text.
    """

    extension = os.path.splitext(
        file_path
    )[1].lower()

    if extension == ".pdf":

        return extract_text_from_pdf(
            file_path
        )

    elif extension == ".txt":

        return extract_text_from_txt(
            file_path
        )

    else:

        raise ValueError(
            "Only PDF and TXT files are supported."
        )

