import joblib
import numpy as np
import pandas as pd
import streamlit as st


MODEL_PATH = "models/student_model.joblib"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


def prepare_input(study_hours, attendance, previous_score, sleep_hours, stress_level):
    return np.array([[
        study_hours,
        attendance,
        previous_score,
        sleep_hours,
        stress_level
    ]])


def get_risk_level(pass_probability):
    if pass_probability >= 0.75:
        return "High chance of passing", "green"
    elif pass_probability >= 0.50:
        return "Moderate chance of passing", "orange"
    else:
        return "Low chance of passing", "red"


st.set_page_config(
    page_title="Student Exam Success Predictor",
    page_icon="🎓",
    layout="centered"
)

model = load_model()

st.title("🎓 Student Exam Success Predictor")
st.write(
    "A simple machine learning application that predicts whether a student "
    "is likely to pass an exam based on learning habits and academic indicators."
)

st.divider()

st.header("Student information")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider(
        "Study hours per day",
        min_value=0,
        max_value=12,
        value=5,
        help="Average number of hours spent studying per day."
    )

    attendance = st.slider(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=75,
        help="Percentage of attended classes."
    )

    previous_score = st.slider(
        "Previous exam score",
        min_value=0,
        max_value=100,
        value=60,
        help="Score obtained in a previous exam or assessment."
    )

with col2:
    sleep_hours = st.slider(
        "Sleep hours per night",
        min_value=0,
        max_value=12,
        value=7,
        help="Average number of hours of sleep per night."
    )

    stress_level = st.slider(
        "Stress level (1-10)",
        min_value=1,
        max_value=10,
        value=5,
        help="Self-reported stress level, where 1 is very low and 10 is very high."
    )

st.divider()

if st.button("Predict exam result", type="primary", use_container_width=True):
    input_data = prepare_input(
        study_hours,
        attendance,
        previous_score,
        sleep_hours,
        stress_level
    )

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    fail_probability = probabilities[0]
    pass_probability = probabilities[1]

    st.header("Prediction result")

    if prediction == 1:
        st.success("Prediction: PASS ✅")
    else:
        st.error("Prediction: FAIL ❌")

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.metric("Pass probability", f"{pass_probability:.2%}")

    with metric_col2:
        st.metric("Fail probability", f"{fail_probability:.2%}")

    risk_label, risk_color = get_risk_level(pass_probability)
    st.markdown(f"**Assessment:** :{risk_color}[{risk_label}]")

    st.subheader("Input summary")

    summary_df = pd.DataFrame({
        "Feature": [
            "Study hours per day",
            "Attendance",
            "Previous exam score",
            "Sleep hours per night",
            "Stress level"
        ],
        "Value": [
            study_hours,
            f"{attendance}%",
            previous_score,
            sleep_hours,
            stress_level
        ]
    })

    st.dataframe(summary_df, use_container_width=True, hide_index=True)

else:
    st.info("Adjust the values above and click the prediction button.")