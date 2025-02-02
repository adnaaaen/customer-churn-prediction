
Custmer Churn Prediction
========================
<div align="center">
  
![Python](https://img.shields.io/badge/Python-000000?style=flat&logo=python&logoColor=white&labelColor=000000&border-radius=12)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white&labelColor=000000&border-radius=12)
![Sklearn](https://img.shields.io/badge/Scikit--Learn-000000?style=flat&logo=scikit-learn&logoColor=white&labelColor=000000&border-radius=12)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-000000?style=flat&logo=github-actions&logoColor=white&labelColor=000000&border-radius=12)
![HTML](https://img.shields.io/badge/HTML-000000?style=flat&logo=html5&logoColor=white&labelColor=000000&border-radius=12)
![CSS](https://img.shields.io/badge/CSS-000000?style=flat&logo=css3&logoColor=white&labelColor=000000&border-radius=12)
![Pandas](https://img.shields.io/badge/Pandas-000000?style=flat&logo=pandas&logoColor=white&labelColor=000000&border-radius=12)
![Numpy](https://img.shields.io/badge/Numpy-000000?style=flat&logo=numpy&logoColor=white&labelColor=000000&border-radius=12)
![PyTest](https://img.shields.io/badge/Pytest-000000?style=flat&logo=pytest&logoColor=white&labelColor=000000&border-radius=12)
![Test](https://github.com/adnaen/customer-churn-prediction/actions/workflows/ci-test.yml/badge.svg)
</div>


**About the Project**

This is a **Customer Churn Prediction** application that predicts whether a customer is likely to churn based on historical data. The application follows a robust **pipeline-based workflow** for preprocessing, model building, and evaluation. It also includes a **Flask web application** for easy user interaction and is containerized using **Docker** for seamless deployment and scalability.

**Workflow**

The application workflow is structured as follows:

1. **Data Ingestion**:
   - Load the dataset from a CSV file.
2. **Data Cleaning and Preprocessing**:
   - Handle missing values.
   - Encode categorical variables.
   - Normalize/standardize numerical features.

4. **Pipeline Creation**:
   - Build a pipeline using `scikit-learn` to streamline preprocessing and model training.
   - Save the pipeline using `joblib` for reuse.

5. **Model Building and Evaluation**:
   - Train multiple classification models.
   - Evaluate models using metrics such as accuracy, precision, recall, and F1-score.
   - Select the best-performing model.
---

**Key Features**

- End-to-end machine learning pipeline for classification tasks.
- Modular and reusable code for data preprocessing and model training.
- Simple and intuitive web interface built with Flask.
- Fully containerized setup for deployment using Docker.
