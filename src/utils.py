"""
Script fungsi utilitas bantuan untuk proyek ini.
Author: Wildan Zakaria-15768
"""
import os

def check_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Direktori {path} berhasil dibuat.")