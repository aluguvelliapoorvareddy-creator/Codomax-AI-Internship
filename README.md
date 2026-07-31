# Student Exam Score Predictor App

An interactive Python machine learning application built during the Codomax internship. The app uses a Linear Regression algorithm to analyze student learning habits and forecast potential examination score outputs based on inputted continuous study hours.

## 📁 Project Architecture
```text
student_score_predictor/
│
├── models/
│   └── score_predictor_model.pkl  # Serialized model artifact
├── main.py                         # Interactive app entry point
├── train.py                        # Model pipeline and data fitting
└── utils.py                        # Centralized helper configuration
```

## 🛠️ Installation & Setup
1. Clone the project repository framework locally:
   ```bash
   git clone https://github.com
   cd student_score_predictor
   ```
2. Install required scikit-learn dependency tracking modules:
   ```bash
   pip install pandas numpy scikit-learn joblib
   ```

## 🚀 How to Execute
First, execute the back-end machine learning configuration loop to fit and serialize your core weights matrix to disk:
```bash
python train.py
```

Next, run the front-end user terminal interface engine to interactively test incoming inputs:
```bash
python main.py
```

## 📊 Expected Outcomes
- **Training Stage:** Automatically fits the data trends and saves an optimized `.pkl` predictive module file.
- **Application Interface:** Provides responsive prediction error handling and input data safety checks.
-