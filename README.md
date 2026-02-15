 HEAD
# Student Data Automation & Ranking System (Python)

A Python-based automation tool to process and organize student data collected via Google Forms (Excel/CSV).
It supports cleaning, sorting (single/multi-column), optional filtering, ranking (Top N), and exporting results.

## Features
- Excel/CSV input support
- Column normalization + basic cleaning
- Multi-column sorting (e.g., cgpa -> name -> usn)
- Optional filtering (e.g., section = A)
- Ranking based on a score column (dense rank)
- Export to Excel and CSV

## Tech Stack
- Python
- Pandas
- File Handling
- Data Structures (sorting/searching logic)

## Setup
```bash
pip install -r requirements.txt
python src/main.py

# student_data_automation
my first project

