import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# -------------------------------
# 🔹 Project Description
# -------------------------------
st.markdown("""
## 🎓 Student Placement Prediction System

This system predicts student placement chances based on:
- Academic performance (CGPA)
- Skills & projects
- Internship experience
- Coding proficiency
""")

# -------------------------------
# 🔹 Load Dataset
# -------------------------------
df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\college_students_skills_vs_placement_reality.csv")
df.columns = df.columns.str.strip()

# -------------------------------
# 🔹 Prepare Data
# -------------------------------
y = df['placement_status']
X = df.drop(['placement_status', 'job_role', 'package_lpa'], axis=1, errors='ignore')
X = pd.get_dummies(X, drop_first=True)

# -------------------------------
# 🔹 Train Model
# -------------------------------
model = RandomForestClassifier()
model.fit(X, y)
# -------------------------------
# 🔹 Feature Importance
# -------------------------------
importance = model.feature_importances_
feature_names = X.columns

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
}).sort_values(by='Importance', ascending=False)

# Show top 10
st.write("### 📊 Top Factors Affecting Placement")
st.dataframe(importance_df.head(10))

# Plot chart
st.bar_chart(importance_df.set_index('Feature').head(10))

# -------------------------------
# 🔹 UI Inputs
# -------------------------------
st.write("### Enter Student Details")

age = st.slider("Age", 18, 30, 22)
cgpa = st.slider("CGPA", 5.0, 10.0, 7.0)
skills = st.slider("Skills Count", 1, 15, 5)
internships = st.slider("Internships", 0, 5, 1)
projects = st.slider("Projects", 0, 10, 2)

gender = st.selectbox("Gender", ["M", "F"])
degree = st.selectbox("Degree", ["B.Tech", "BCA", "B.Sc"])
branch = st.selectbox("Branch", ["CSE", "IT", "Data Science", "Commerce"])
college_tier = st.selectbox("College Tier", ["Tier-1", "Tier-2", "Tier-3"])
coding_level = st.selectbox("Coding Level", ["Basic", "Intermediate", "Advanced"])
with st.expander("📊 Show Feature Importance"):
    st.dataframe(importance_df.head(10))
    st.bar_chart(importance_df.set_index('Feature').head(10))

# -------------------------------
# 🔹 Convert Input → DataFrame
# -------------------------------
input_data = pd.DataFrame({
    'age': [age],
    'skills_count': [skills],
    'internships': [internships],
    'projects': [projects],
    'cgpa': [cgpa],
    'gender': [gender],
    'degree': [degree],
    'branch': [branch],
    'college_tier': [college_tier],
    'coding_level': [coding_level]
})

# Encode input
input_data = pd.get_dummies(input_data)

# Align with training data
input_data = input_data.reindex(columns=X.columns, fill_value=0)

# -------------------------------
# 🔹 Prediction Logic
# -------------------------------
if st.button("Predict Placement"):
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    # Get probability of "Placed"
    placed_prob = proba[list(model.classes_).index("Placed")]

    # Output
    if prediction == "Placed":
        st.success(f"🎉 High chances of placement ({placed_prob*100:.2f}%)")
    else:
        st.warning(f"⚠️ Low chances of placement ({placed_prob*100:.2f}%)")

    # Show probability
    st.write(f"Probability of Placement: {placed_prob*100:.2f}%")

    # Progress bar
    st.progress(int(placed_prob * 100))