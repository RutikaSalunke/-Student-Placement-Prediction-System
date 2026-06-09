# Student-Placement-Prediction-System
Student Placement Prediction System using Python, Streamlit, Pandas, and Random Forest Classifier with feature importance analysis and placement probability prediction.
Overview

The Student Placement Prediction System is a Machine Learning web application built using Streamlit and Scikit-Learn. The application predicts whether a student is likely to be placed based on academic performance, technical skills, internship experience, project work, and coding proficiency.

The system uses a Random Forest Classifier trained on a student placement dataset and provides both placement prediction and placement probability.

Features

✅ Student placement prediction

✅ Placement probability score

✅ Feature importance analysis

✅ Interactive Streamlit dashboard

✅ Visual representation of important placement factors

✅ User-friendly input form

Dataset

The project uses the dataset:

college_students_skills_vs_placement_reality.csv

Input Features
Age
CGPA
Skills Count
Internship Count
Project Count
Gender
Degree
Branch
College Tier
Coding Level
Target Variable
Placement Status
Placed
Not Placed
Machine Learning Model
Algorithm Used

Random Forest Classifier

Reason for selection:

Handles categorical and numerical data effectively
Reduces overfitting through ensemble learning
Provides feature importance scores
Delivers reliable classification performance
Project Workflow
1. Data Loading

The dataset is loaded using Pandas and column names are cleaned to avoid formatting issues.

2. Data Preprocessing
Unnecessary columns are removed:
job_role
package_lpa
Categorical variables are converted using One-Hot Encoding.
3. Model Training

A Random Forest Classifier is trained using the processed dataset.

4. Feature Importance

The trained model calculates feature importance values to identify which factors contribute most to placement prediction.

5. User Input

The user provides:

Academic details
Skill information
Internship experience
Project experience
Coding proficiency
6. Prediction

The model predicts:

Placement Status
Probability of Placement (%)
Application Screens
Home Page

Users can enter student details through interactive sliders and dropdown menus.

Feature Importance

The application displays the top features affecting placement using:

Data Table
Bar Chart
Prediction Result

After clicking Predict Placement, the application displays:

Placement prediction
Placement probability
Progress indicator
Technologies Used
Technology	Purpose
Python	Programming Language
Streamlit	Web Application Framework
Pandas	Data Processing
Scikit-Learn	Machine Learning
Random Forest	Classification Model
Installation
Clone Repository
git clone https://github.com/rutikasalunke/student-placement-prediction-system.git
Install Dependencies
pip install -r requirements.txt
Run Application
streamlit run app.py
Future Enhancements
Model performance evaluation metrics
Hyperparameter tuning
Job role prediction
Package prediction
Resume analysis integration
Deployment on Streamlit Cloud
Author

Rutika Salunke

B.Tech – Computer Science and Design

Data Analytics | Machine Learning | Power BI | Research
