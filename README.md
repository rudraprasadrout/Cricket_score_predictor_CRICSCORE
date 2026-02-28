# 🏏 CRICSCORE: Cricket Score Predictor

A data-driven machine learning application designed to predict the final scores of cricket matches (IPL/T20/ODI). By analyzing historical ball-by-ball data, **CRICSCORE** provides real-time projections based on current match momentum.

---

## 🚀 Key Features

* **Multi-Format Analysis:** Supports score predictions for International and League (IPL) formats.
* **Dynamic Inputs:** Predicts based on real-time variables like current runs, wickets, and overs.
* **Momentum Tracking:** Factors in performance from the "Last 5 Overs" to account for death-over acceleration or mid-innings collapses.
* **Optimized Accuracy:** Utilizes regression-based algorithms for precise score estimation.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **Data Handling** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn (Linear Regression / Random Forest) |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Flask / Streamlit (Optional) |

---

## 📊 Data & Methodology

The model follows a standard ML pipeline to ensure reliability:

1.  **Data Acquisition:** Ball-by-ball data including venue, batting/bowling teams, and match state.
2.  **Feature Engineering:**
    * One-Hot Encoding for categorical data (Teams, Venues).
    * Rolling calculations for "Runs in Last 5 Overs" and "Wickets in Last 5 Overs."
3.  **Model Selection:** Testing across various regressors to minimize Mean Absolute Error (MAE).
4.  **Persistence:** The trained model is serialized using `pickle` for instant loading.

---

## 📂 Project Structure

```plaintext
Cricket_score_predictor_CRICSCORE/
├── datasets/            # Raw and processed CSV files
├── models/              # Saved .pkl files for the trained models
├── notebooks/           # Jupyter notebooks for Exploratory Data Analysis
├── src/                 # Source code for training and prediction
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
---

## 💻 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/rudraprasadrout/Cricket_score_predictor_CRICSCORE.git](https://github.com/rudraprasadrout/Cricket_score_predictor_CRICSCORE.git)
cd Cricket_score_predictor_CRICSCORE
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
Markdown
### 3. Run the Predictor

```python
import pickle
```
# Example: Load model and predict
model = pickle.load(open('models/score_model.pkl', 'rb'))

# Input: [Batting_Team, Bowling_Team, Runs, Wickets, Overs, Runs_last_5, Wickets_last_5]
prediction = model.predict(your_input_array)
print(f"Projected Score: {int(prediction[0])}")
---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**.

1. **Fork** the Project.
2. **Create** your Feature Branch 
   ```bash
   git checkout -b feature/NewPredictionModel

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.

**Developed by [Rudra Prasad Rout](https://github.com/rudraprasadrout)**
