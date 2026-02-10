import pickle

import numpy as np
import pandas as pd
import streamlit as st

# Load model
model = pickle.load(open('diabetes_model.pkl','rb'))

st.title("Diabetes Prediction")

feature_names = getattr(model, "feature_names_in_", None)
if feature_names is None:
    st.error(
        "Model does not expose feature names. Please retrain and save a full pipeline "
        "(preprocessing + model) or save the feature list used in training."
    )
else:
    st.write("Provide values for all required features:")
    inputs = {}
    for name in feature_names:
        default_value = 0.0
        if name.lower() in {"age", "glucose", "bmi"}:
            default_value = 0.0
        inputs[name] = st.number_input(name, value=default_value)

    if st.button("Predict"):
        features_df = pd.DataFrame([inputs], columns=feature_names)
        result = model.predict(features_df)[0]
        st.write("Diabetes Risk:", "Positive" if result == 1 else "Negative")
