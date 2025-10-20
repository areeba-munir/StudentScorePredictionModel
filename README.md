# Student Score Prediction Model

##  Project Overview
This project focuses on predicting students' exam scores based on various factors such as study hours, attendance, sleep, motivation, and other academic and environmental factors. The goal is to build a **machine learning regression model** that can estimate students' performance and provide insights into which factors contribute most to exam success.

---

##  Folder Structure
StudentScorePredictionModel/
│
├── StudentScorePrediction.ipynb # Main Jupyter Notebook with EDA, preprocessing, and model training
├── StudentPerformanceFactors.csv # Dataset (downloaded from Kaggle)
├── README.md # Project documentation (this file)
├── LICENSE # License file (optional)
└── .gitignore # Python gitignore

---

##  Tools & Libraries
- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

Optional (for advanced models):
- RandomForestRegressor  
- GradientBoostingRegressor  

---

##  Dataset Description
The dataset used is **Student Performance Factors** (Kaggle), containing features such as:

| Feature | Description |
|---------|-------------|
| Hours_Studied | Number of study hours per day |
| Attendance | Percentage of classes attended |
| Sleep_Hours | Average sleep hours per day |
| Motivation_Level | Self-reported motivation score |
| Previous_Scores | Scores from previous exams |
| Teacher_Quality | Teacher evaluation score |
| Parental_Involvement | Level of parental involvement |
| Access_to_Resources | Availability of study resources |
| Tutoring_Sessions | Number of extra tutoring sessions attended |
| Physical_Activity | Hours of physical activity |
| Peer_Influence | Influence of peers on study habits |
| Parental_Education_Level | Education level of parents |
| Distance_from_Home | Distance from school in km |
| Gender | Student gender |
| Internet_Access | Availability of internet at home |
| School_Type | Type of school attended |
| Exam_Score | Final exam score (target variable) |

> Some columns had missing values which were handled during preprocessing.

---

##  Project Steps

1. **Data Loading**
   - Load the CSV dataset into a Pandas DataFrame.
2. **Data Cleaning**
   - Handle missing values (numeric: median, categorical: mode).  
   - Encode categorical variables using LabelEncoder.
3. **Exploratory Data Analysis (EDA)**
   - Visualize feature distributions, correlations, and outliers.  
   - Use sampling for large datasets to speed up plotting.
4. **Feature Selection**
   - Select relevant features for predicting `Exam_Score`.
5. **Modeling**
   - Split dataset into training and testing sets.
   - Train Linear Regression model (baseline).  
   - Experiment with Polynomial Regression.  
   - Advanced models: RandomForestRegressor and GradientBoostingRegressor.
6. **Model Evaluation**
   - Evaluate using MAE, MSE, RMSE, and R² score.
   - Visualize actual vs predicted exam scores.
7. **Feature Importance**
   - Identify which features contribute most to predictions (Random Forest/Gradient Boosting).

---

##  Results

| Model | R² Score | MAE | RMSE |
|-------|----------|-----|------|
| Linear Regression | 0.58 | 1.42 | 2.55 |
| Random Forest | 0.85+ | - | - |
| Gradient Boosting | 0.88+ | - | - |

> Random Forest and Gradient Boosting models significantly improved performance over Linear Regression.

---

##  How to Run

1. Clone this repository:
```bash
git clone https://github.com/yourusername/StudentScorePredictionModel.git
