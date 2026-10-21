# Iris Flower Classification Using Machine Learning

## About the Project

This is a beginner-friendly Machine Learning web application that predicts the species of an Iris flower based on four measurements. The application is built using Python and Streamlit.

## Features

- Predicts the Iris flower species from user-entered measurements.
- Uses a trained Machine Learning model.
- Displays the predicted flower species.
- Shows the corresponding flower image.
- Displays the measurements entered by the user.

## Technologies Used

- Python
- Machine Learning
- Scikit-learn
- Streamlit
- Pandas
- Joblib

## Flower Species

The model predicts one of three Iris species:

- Iris setosa
- Iris versicolor
- Iris virginica

## Project Structure

```text
Iris_ML_Project/
├── app.py
├── iris_model.pkl
├── images/
│   ├── setosa.jpg
│   ├── versicolor.jpg
│   └── virginica.jpg
├── requirements.txt
└── README.md
```

## How to Run the Project in VS Code

1. Install Python and Visual Studio Code.
2. Open the `Iris_ML_Project` folder in VS Code.
3. Open the integrated terminal using **Terminal → New Terminal**.
4. Create a virtual environment if you don't already have one:

   ```powershell
   python -m venv .venv
   ```

5. Activate the virtual environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

6. Install the required packages:

   ```powershell
   pip install -r requirements.txt
   ```

7. Start the application:

   ```powershell
   streamlit run app.py
   ```

8. Open the local URL displayed in the terminal, usually `http://localhost:8501`.


## Purpose

This project demonstrates how a trained Machine Learning model can be integrated into a simple web application to make predictions from user input.

## Project Status

Completed beginner-level Iris flower classification application. Future improvements may include prediction probabilities, model evaluation, and a more detailed user interface.
