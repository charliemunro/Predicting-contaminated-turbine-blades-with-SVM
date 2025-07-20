# Predicting Contaminated Turbine Blades with SVM

A machine learning pipeline using Support Vector Machines (SVM) to predict contamination in turbine blades from sensor data.

---

## 📁 Project Structure

```
predicting-contaminated-turbine-blades-with-svm/
├── data/
│   ├── raw/                   # Original datasets (CSV files)
│   ├── processed/             # Cleaned and feature-engineered data
│   └── sample.csv             # Sample rows for quick testing
├── notebooks/
│   └── analysis.ipynb         # Jupyter notebook with exploratory analysis
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py       # Data loading & preprocessing
│   ├── model.py               # SVM training and evaluation
│   └── utils.py               # Helper functions (feature selection, plotting)
├── tests/
│   ├── test_data_pipeline.py  # Tests for data transformations
│   └── test_model.py          # Tests for model predictions
├── .github/
│   └── workflows/ci.yml       # CI workflow for linting & tests
├── requirements.txt           # Python dependencies
├── setup.py                   # Package install script
├── README.md                  # This file
└── LICENSE                    # Open-source license
```

---

## 📖 Overview

This project implements a classification pipeline to detect contaminated turbine blades based on sensor measurements. It includes:

- **Data preprocessing**: cleaning, feature engineering, and scaling  
- **Modeling**: training an SVM classifier with hyperparameter tuning  
- **Evaluation**: performance metrics, confusion matrix, ROC curves  
- **Notebooks**: exploratory data analysis and results visualization  

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/charliemunro/predicting-contaminated-turbine-blades-with-svm.git
cd predicting-contaminated-turbine-blades-with-svm

# Optional: set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# Or install as a package
pip install .
```

---

## 🎯 Usage

### As a Package

```python
from src.model import train_and_evaluate
from src.data_pipeline import load_data

# Load processed dataset
X_train, X_test, y_train, y_test = load_data("data/processed/dataset.csv")

# Train and evaluate SVM
results = train_and_evaluate(X_train, X_test, y_train, y_test)
print(results.classification_report)
```

### Jupyter Notebook

```bash
jupyter notebook notebooks/analysis.ipynb
```

Explore data distributions, train models interactively, and visualize results.

---

## 🔧 Testing & CI

- **pytest** is used for unit tests in `tests/`.
- **GitHub Actions** CI is configured to run lint checks and tests on every push.

```bash
# Run all tests locally
pytest
```

---

## 🤝 Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on reporting issues and submitting pull requests.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🔖 Topics

`python` · `machine-learning` · `svm` · `data-processing` · `jupyter-notebook`
