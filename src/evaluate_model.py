"""
Script untuk mengevaluasi performa model menggunakan metrik klasifikasi.
Author: Wildan Zakaria-15768
"""
from sklearn.metrics import accuracy_score, classification_report

def evaluate_predictions(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    print(f"Accuracy: {acc:.4f}")
    return acc

if __name__ == "__main__":
    print("Modul evaluasi siap digunakan.")