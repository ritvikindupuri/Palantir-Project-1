# Palantir Foundry IoT Sensor ETL Pipeline & ML Analysis

This project demonstrates a comprehensive, end-to-end data engineering and data science workflow using Palantir Foundry. It includes a production-ready ETL pipeline with AI-powered transformations, as well as a separate machine learning analysis with rich visualizations. This project is designed to showcase a strong set of skills for a developer role at Palantir.

## Project Overview

The goal of this project is to process raw IoT sensor data, clean and transform it, and then perform advanced analysis to extract meaningful insights. The project is divided into two main components:

1.  **Palantir Foundry ETL Pipeline**: A multi-stage pipeline that cleans, enriches, and aggregates the sensor data.
2.  **Python-Based ML Analysis**: A separate data science analysis that uses the pipeline's output to perform anomaly detection and create insightful visualizations.

## 1. Palantir Foundry ETL Pipeline

The core of this project is a robust ETL pipeline built in Palantir Foundry. The pipeline is deployed and fully operational.

### Pipeline Architecture

The pipeline consists of four main stages:

1.  **Input Data**: The pipeline starts with the `cde_ipaas_dataset`, which contains raw IoT sensor data with 9 columns.
2.  **Data Quality & Feature Engineering**: This stage uses AI-generated transformations to clean the data, remove duplicates, and create 4 new feature columns, resulting in a 13-column dataset.
3.  **Aggregation**: The data is then aggregated by `sensor_type` to calculate the average efficiency ratio for each sensor.
4.  **Output Data**: The final output is a clean, aggregated dataset named `sensor_performance_summary` with 2 columns.

<br>

<p align="center">
  <img src="pipeline_deployed.png" alt="Palantir Foundry Pipeline" width="800"/>
  <br>
  <em>Figure 1: The complete, deployed ETL pipeline in Palantir Foundry.</em>
</p>

<br>

### AI Features in the Pipeline

This pipeline leverages Foundry’s AI capabilities to automate and enhance the data transformation process:

-   **AI-Assisted Transformation Generation**: The data quality and feature engineering logic was generated from natural language prompts, demonstrating the ability to use cutting-edge AI tools.
-   **Smart Feature Engineering**: The pipeline automatically creates key performance indicators such as `energy_efficiency_ratio` and `performance_score`.
-   **Intelligent Data Quality**: AI-driven deduplication and filtering ensure the data is clean and reliable.

## 2. Python-Based ML Analysis & Visualizations

To showcase advanced data science skills, I performed a separate analysis on the pipeline's data using Python, `scikit-learn`, and `matplotlib`.

### Machine Learning Anomaly Detection

I used the **Isolation Forest** algorithm to identify anomalous sensor readings. This unsupervised learning method is highly effective for outlier detection.

-   **Results**: The model identified 10% of the records as anomalies, which are visualized in the scatter plot below.

<br>

<p align="center">
  <img src="anomaly_detection_scatter.png" alt="Anomaly Detection Scatter Plot" width="700"/>
  <br>
  <em>Figure 2: Anomaly detection results using the Isolation Forest algorithm.</em>
</p>

<br>

### Data Visualizations

I created a series of visualizations to provide a clear and insightful overview of the sensor data.

#### Sensor Performance Dashboard

This dashboard provides a multi-faceted view of sensor performance, combining aggregated metrics with detailed distributions.

<br>

<p align="center">
  <img src="performance_dashboard.png" alt="Sensor Performance Dashboard" width="800"/>
  <br>
  <em>Figure 3: A comprehensive dashboard of sensor performance metrics.</em>
</p>

<br>

**Key Insights from the Dashboard:**

-   `ECG` and `PulseOximeter` sensors have the highest average efficiency.
-   `PulseOximeter` and `Accelerometer` sensors exhibit the most anomalies.

#### Correlation Matrix

This heatmap reveals the relationships between different sensor metrics, which is crucial for feature engineering and understanding the data.

<br>

<p align="center">
  <img src="correlation_heatmap.png" alt="Correlation Matrix" width="600"/>
  <br>
  <em>Figure 4: Correlation matrix of key sensor performance metrics.</em>
</p>

<br>

## Conclusion

This project demonstrates a full-cycle data workflow, from ETL pipeline construction to advanced machine learning analysis and visualization. It showcases a strong command of Palantir Foundry, data engineering principles, and data science techniques, making it a compelling project for a Palantir developer application.
