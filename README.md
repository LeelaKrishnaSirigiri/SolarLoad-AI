# ☀️ SolarLoad AI — Electricity Bill to Solar Load Automation

This project automates the process of converting electricity bill data into a solar load calculation Excel sheet.

## 🚀 Overview

Energybae currently analyzes electricity bills manually to calculate solar system requirements. This tool automates that workflow:

Upload bill → Extract data → Fill Excel → Get output instantly

---

## 🧠 What it does

- Upload MSEDCL electricity bill (image)
- Extract key fields using OCR:
  - Consumer Name
  - Consumer Number
  - Units Consumed
  - Sanctioned Load
  - Connection Type
  - Bill Amount
- Fill the provided Excel template automatically
- Preserve all Excel formulas
- Allow manual review/edit for accuracy

---

## ⚙️ Tech Stack

- Python
- Streamlit (UI)
- OpenCV (image processing)
- Tesseract OCR (text extraction)
- OpenPyXL (Excel automation)

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py