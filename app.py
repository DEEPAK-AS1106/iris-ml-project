
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Find the images folder
IMAGE_DIR = Path(__file__).parent / "images"

FLOWER_IMAGES = {
    "Iris setosa": IMAGE_DIR / "setosa.jpg",
    "Iris versicolor": IMAGE_DIR / "versicolor.jpg",
    "Iris virginica": IMAGE_DIR / "virginica.jpg",
}

# Load the trained machine learning model
MODEL_PATH = Path(__file__).parent / "iris_model.pkl"
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

st.title("🌸 Iris Flower Species Classification")
st.write(
    "Enter the flower measurements below "
    "and click Predict to identify its species."
)

st.divider()
st.subheader("Enter Flower Measurements")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal length (cm)",
        min_value=0.1,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    petal_length = st.number_input(
        "Petal length (cm)",
        min_value=0.1,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

with col2:
    sepal_width = st.number_input(
        "Sepal width (cm)",
        min_value=0.1,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal width (cm)",
        min_value=0.1,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

# Predict only when the button is clicked
if st.button("Predict Flower Species", type="primary"):

    input_data = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)"
        ]
    )

    prediction = model.predict(input_data)[0]

    species_names = [
        "Iris setosa",
        "Iris versicolor",
        "Iris virginica"
    ]

    predicted_species = species_names[int(prediction)]

    # Show the prediction
    st.success(f"Predicted Species: {predicted_species}")

    # Show the matching flower image
    image_path = FLOWER_IMAGES[predicted_species]

    if image_path.exists():
        st.image(
            str(image_path),
            caption=predicted_species,
            width=400
        )
    else:
        st.warning(
            f"Image not found: {image_path.name}. "
            "Please check your images folder."
        )

    # Show the measurements entered
    st.write("Measurements entered:")
    st.dataframe(input_data, hide_index=True)
