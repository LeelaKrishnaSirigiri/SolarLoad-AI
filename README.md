#  SolarLoad AI — Electricity Bill to Solar Load Automation

This project automates the process of converting electricity bill data into a solar load calculation Excel sheet.

##  Overview

Energybae currently analyzes electricity bills manually to calculate solar system requirements. This tool automates that workflow:

Upload bill → Extract data → Fill Excel → Get output instantly

---

## What it does

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

## Tech Stack

- Python
- Streamlit (UI)
- OpenCV (image processing)
- Tesseract OCR (text extraction)
- OpenPyXL (Excel automation)

---

## 🛠️ How to Run

- pip install -r requirements.txt
- streamlit run app.py 
---

##  Project Structure

SolarLoad-AI/  
│  
├── app.py                 # Streamlit UI  
├── extractor.py           # OCR + data extraction  
├── excel_filler.py        # Excel automation  
├── requirements.txt  
├── README.md  

├── input/  
│   └── template.xlsx      # Provided Excel template  

├── output/  
│   └── .gitkeep  

---

##  Notes & Assumptions

- Monthly consumption history in the bill appears as a low-resolution graph with regional language labels, which makes fully automatic extraction unreliable.  
- A manual review/edit step is included to ensure the final Excel output remains accurate.  
- Fixed charges are defaulted when OCR cannot reliably extract them.  

---

##  Future Improvements

- Improve OCR accuracy using Google Vision API  
- Add support for PDF bills  
- Better extraction of monthly consumption history  
- Support for multiple electricity boards  

---


##  Outcome

This system reduces manual effort from 15–30 minutes to under 1 minute per bill, while maintaining accuracy through a review step.

---

## Author

Leela Krishna  
AI Intern Task Submission — Energybae
