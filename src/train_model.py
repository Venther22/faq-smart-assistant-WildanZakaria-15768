"""
Script untuk melatih model Machine Learning (XGBoost & Logistic Regression).
Author: Wildan Zakaria-15768
"""
import pickle

def save_model(model, filename):
    with open(f'../models/{filename}', 'wb') as f:
        pickle.dump(model, f)
    print(f"Model tersimpan di {filename}")

if __name__ == "__main__":
    print("Modul training siap digunakan. Training utama dilakukan di notebooks/02_modeling.ipynb")