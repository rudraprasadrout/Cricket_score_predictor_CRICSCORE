# 🏏 CRICSCORE: IPL Score Predictor

Predicting the pulse of the game using Machine Learning.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![ML](https://img.shields.io/badge/ML-Linear%20Regression-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Overview
**CRICSCORE** is a machine learning-based web application designed to predict the final score of an IPL match based on current match dynamics. By analyzing historical data, the model provides real-time estimations of how the first innings will conclude.

## 🚀 Features
* **Real-time Prediction:** Input current overs, wickets, and runs to get an instant projected score.
* **Venue & Team Intelligence:** Accounts for specific team strengths and stadium scoring patterns.
* **Interactive UI:** Clean, modern interface built with **Streamlit**.
* **Historical Accuracy:** Trained on extensive IPL datasets.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn |
| **Deployment** | Streamlit |

---

## 📁 Project Structure
```text
├── data/               # Raw and processed datasets
├── models/             # Trained .pkl files
├── notebooks/          # Data cleaning & Model training (Jupyter)
├── app.py              # Main Streamlit application
└── requirements.txt    # Project dependencies
```
## ⚙️ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone [https://github.com/rudraprasadrout/Cricket_score_predictor_CRICSCORE.git](https://github.com/rudraprasadrout/Cricket_score_predictor_CRICSCORE.git)
   cd Cricket_score_predictor_CRICSCORE
   ```
### 2. Install dependencies

Install the necessary Python libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```
### 3. Run the App

Launch the **Streamlit** web application locally by executing:

   ```bash
   streamlit run app.py
   ```
---

## 📊 How it Works

The model utilizes a **regression-based approach** to estimate the final score. By analyzing historical match data, the prediction logic follows this mathematical foundation:

$$Score_{predicted} = \beta_0 + \beta_1(Runs) + \beta_2(Wickets) + \beta_3(Overs) + \dots + \epsilon$$

> [!TIP]
> **Performance Note:** The model performs best after the **first 5 overs** of play, as early-game volatility is high.

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Feel free to contribute by following these steps:

1. **Fork** the Project.
2. Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the Branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---

## 👤 Author

**Rudra Prasad Rout**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rudraprasadrout)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/routrp07)
