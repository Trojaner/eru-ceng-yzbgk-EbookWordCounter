#!/usr/bin/env python3

import docx2txt
import ebooklib
from ebooklib import epub
import os.path
import PyPDF2
import re


def get_text(file_path: str):
    extension = os.path.splitext(file_path)[1]
    text = ""

    if extension == ".epub":
        book = epub.read_epub(file_path)
        for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            text += doc.get_content().decode("utf-8")

    elif extension == ".docx":
        text += docx2txt.process(file_path)

    elif extension == ".mobi":
        print("[!] Unsupported file: " + file_path)
        return None

    elif extension == ".pdf":
        pdf_file = open(file_path, "r")
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for x in range(number_of_pages):
            page = read_pdf.getPage(x)
            text += page.extractText()
    else:
        if not extension == ".txt":
            print("[!] Unkown file type: " + file_path + ", processing raw text...")

        text_file = open(file_path, "r", encoding="utf-8")
        text += text_file.read()

    text = text.strip()
    return text


def count_words_in_text(text: str, wordlist: list):
    if text == "" or text is None:
        return None

    words_count = {}
    for word in wordlist:
        word = word.rstrip()
        words_count[word] = len(re.findall("(?i)\s" + re.escape(word) + "(\s|\.|!|\?|\')", text))

    sorted_words_count = [(k, words_count[k]) for k in sorted(words_count, key=words_count.get, reverse=True)]

    sorted_text = ""
    for word, amount in sorted_words_count:
        sorted_text += word + ": " + str(amount) + "\n"

    return sorted_text
