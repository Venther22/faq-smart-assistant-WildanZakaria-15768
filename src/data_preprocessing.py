"""
Script untuk memproses data mentah menjadi data siap latih.
Author: Wildan Zakaria-15768
"""
import re
import pandas as pd

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text

if __name__ == "__main__":
    print("Modul preprocessing siap digunakan.")