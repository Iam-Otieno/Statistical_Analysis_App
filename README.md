# Statistical Analysis Streamlit App

An interactive and modular Streamlit application designed for quick exploratory data analysis (EDA) on CSV datasets. This app helps users understand their data through descriptive statistics, data summaries, and correlation analysis with an easy-to-use interface.

statistical_analysis_app/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── utils/
│   ├── data_loader.py  # Data loading functions
│   └── data_summary.py # Data summary and display functions
└── README.md           # Project documentation

---

## Features

- **Upload CSV files** via a user-friendly interface
- **View Data Preview** to inspect the uploaded dataset
- **Descriptive Statistics** including count, mean, std, min, max, quartiles, and mode for numeric columns
- **DataFrame Info** summary (data types, non-null counts, memory usage)
- **Missing Values** count per column
- **Unique Values** count per column
- **Data Types** overview
- **Shape** of the dataset (rows, columns)
- **Correlation Matrix** for numeric columns
- **Dynamic Column Selection** for tailored descriptive statistics

---

## Installation

### Prerequisites

- Python 3.8 or higher installed on your system
- Git (optional, for cloning the repo)

### Steps

1. Clone the repository (or download the ZIP and extract):

```bash
git clone https://github.com/yourusername/statistical_analysis_app.git
cd statistical_analysis_app

### Troubleshooting
UnicodeDecodeError when loading CSV:
Some CSV files contain special characters or non-UTF8 encoding. Try saving your CSV as UTF-8 encoding or specify encoding in data_loader.py (e.g., pd.read_csv(file, encoding='latin1')).

Streamlit doesn't open automatically:
Copy the local URL shown in the terminal and paste it manually into your browser.
