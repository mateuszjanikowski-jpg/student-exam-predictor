import os
import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


RANDOM_STATE = 42
N_SAMPLES = 1000

np.random.seed(RANDOM_STATE)


def generate_dataset(n_samples: int) -> pd.DataFrame:
    study_hours = np.random.randint(0, 11, n_samples)
    attendance = np.random.randint(40, 101, n_samples)
    previous_score = np.random.randint(20, 101, n_samples)
    sleep_hours = np.random.randint(4, 10, n_samples)
    stress_level = np.random.randint(1, 11, n_samples)

    score = (
        study_hours * 0.25
        + attendance * 0.03
        + previous_score * 0.05
        + sleep_hours * 0.20
        - stress_level * 0.30
        + np.random.normal(0, 1.2, n_samples)
    )

    passed = (score > 7.5).astype(int)

    return pd.DataFrame({
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "sleep_hours": sleep_hours,
        "stress_level": stress_level,
        "passed": passed
    })


def main():
    os.makedirs("data", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    df = generate_dataset(N_SAMPLES)
    df.to_csv("data/students.csv", index=False)

    X = df[[
        "study_hours",
        "attendance",
        "previous_score",
        "sleep_hours",
        "stress_level"
    ]]
    y = df["passed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=RANDOM_STATE,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=6,
        random_state=RANDOM_STATE
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    joblib.dump(model, "models/student_model.joblib")

    print("Model trained successfully.")
    print(f"Dataset shape: {df.shape}")
    print(f"Accuracy on test data: {accuracy:.2f}")
    print()
    print(classification_report(y_test, predictions))
    print("Model saved to models/student_model.joblib")
    print("Dataset saved to data/students.csv")


if __name__ == "__main__":
    main()