📊 Student Data Automation & Ranking System (Python)

🔍 Why I built this:
While working with Google Forms and Excel sheets for academic data, I noticed that manual sorting, filtering, and ranking quickly becomes repetitive and error-prone.
This project automates that workflow and focuses on clean data handling and strong fundamentals, not just surface-level output.


🚀 What this project does:
A Python-based command-line tool that:
* Loads CSV / Excel files (Google Forms compatible)
* Cleans messy column names automatically
* Handles missing and inconsistent data safely
* Supports single & multi-column sorting
* Ranks students using dense ranking
* Extracts Top-N performers
* Exports clean, structured results to Excel/CSV

🧠 Key Engineering Ideas Used:
* Defensive file handling (encoding-safe CSV loading)
* Column normalization to handle inconsistent headers
* Stable sorting for predictable multi-column results
* Dense ranking to handle score ties correctly
* Modular design (each file has a single responsibility)
  This project is intentionally built as a foundations-focused system, similar to real internal tools used by teams.

🛠️ Tech Stack:
* Python
* Pandas
* OpenPyXL
* Regular Expressions
* Command-Line Interface (CLI)

📁 Project Structure
student-data-automation/
│
├── data/        # Input files (CSV / Excel)
├── output/      # Generated ranked results
├── src/
│   ├── loader.py
│   ├── cleaner.py
│   ├── sorter.py
│   ├── ranker.py
│   ├── exporter.py
│   └── main.py
│
├── requirements.txt
└── README.md


▶️ How to run:
 pip install -r requirements.txt
 python src/main.py


The program guides you interactively to:
* select file
* apply filters
* choose sorting & ranking logic
* export results

📌 Example Use Cases:
* Rank students by CGPA
* Extract Top-10 performers
* Filter by section or branch
* Clean Google Form responses automatically

⚠️ Limitations (intentional):
* CLI-based (no GUI yet)
* Filtering currently supports equality checks
* Designed for structured tabular data
  These were deliberate choices to keep the focus on correctness and clarity.

🔮 Future Improvements:
* Numeric range filters (e.g., CGPA > 8.5)
* Multiple filter conditions
* Config-based execution (no prompts)
* Unit tests & logging
* Simple web or GUI interface

🎯 What I learned:
* Handling real-world data inconsistencies
* Writing defensive, readable Python code
* Designing modular data pipelines
* Translating messy input into structured output

👤 About Me:
Computer Science Engineering (Artificial Intelligence & Machine Learning) student focused on strong fundamentals, problem solving, and building reliable systems.
Currently seeking Software Engineering Internship opportunities.

⭐ If you’re a recruiter or engineer,
I’d love feedback, suggestions, or a quick conversation about this project or internships.
