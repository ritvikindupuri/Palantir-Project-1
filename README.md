# Palantir Foundry IoT Sensor ETL Pipeline & ML Analysis

This project demonstrates a comprehensive, end-to-end data engineering and data science workflow using Palantir Foundry. It includes a production-ready ETL pipeline with AI-powered transformations, as well as a separate machine learning analysis with rich visualizations. This project showcases a strong set of skills in data engineering and data science.

## Project Overview

The goal of this project is to process raw IoT sensor data from a wireless body sensor network, transforming it into a clean, aggregated dataset ready for advanced analysis. The project showcases the ability to build robust data infrastructure and then leverage that data to generate actionable insights through machine learning.

## Dataset

This project utilizes the **cde_ipaas_dataset**, which represents data transmission across sensors, sink nodes, and cloud applications in a wireless body sensor network. [1]

- **Key Features**: The dataset includes five sensor types (Accelerometer, ECG, Blood Pressure, Pulse Oximeter, Body Temperature), a layered structure (sensor, edge, cloud), and performance attributes like data size, energy consumption, and transmission duration.
- **Target Column**: The dataset includes a `transmission_efficiency_score` derived from key parameters, which is the focus of the analysis.
- **License**: The dataset is available under the CC0: Public Domain license.

## 1. Palantir Foundry ETL Pipeline

The core of this project is a robust ETL pipeline built in Palantir Foundry. The pipeline is deployed and fully operational, demonstrating the ability to build and manage production-grade data systems.

### Pipeline Architecture

The pipeline consists of four main stages:

1.  **Input Data**: The pipeline starts with the `cde_ipaas_dataset`, which contains raw IoT sensor data with 9 columns.
2.  **Data Quality & Feature Engineering**: This stage uses AI-generated transformations to clean the data, remove duplicates, and create 4 new feature columns, resulting in a 13-column dataset.
3.  **Aggregation**: The data is then aggregated by `sensor_type` to calculate the average efficiency ratio for each sensor.
4.  **Output Data**: The final output is a clean, aggregated dataset named `sensor_performance_summary` with 2 columns.

<br>

<p align="center">
  <img src="https://i.imgur.com/hQlrZ7K.png" alt="Palantir Foundry Pipeline" width="800"/>
  <br>
  <em>Figure 1: The complete, deployed ETL pipeline in Palantir Foundry. This demonstrates the ability to build and manage a production-grade data workflow, from raw data ingestion to a clean, aggregated output.</em>
</p>

<br>

### AI Features in the Pipeline

This pipeline leverages Foundry’s AI capabilities to accelerate development and enhance the data transformation process:

-   **AI-Assisted Transformation Generation**: The data quality and feature engineering logic was generated from natural language prompts, demonstrating the ability to use cutting-edge AI tools to rapidly build complex pipelines.
-   **Smart Feature Engineering**: The pipeline automatically creates key performance indicators such as `energy_efficiency_ratio` and `performance_score`.
-   **Intelligent Data Quality**: AI-driven deduplication and filtering ensure the data is clean and reliable.

## 2. Python-Based ML Analysis & Visualizations

To showcase advanced data science skills, I performed a separate analysis on a representative sample of the pipeline's data using Python, `scikit-learn`, and `matplotlib`.

### Machine Learning Anomaly Detection

I used the **Isolation Forest** algorithm to identify anomalous sensor readings. This unsupervised learning method is highly effective for outlier detection. [2]

-   **Results**: The model identified 10% of the records as anomalies. These anomalies represent sensor readings that deviate significantly from the norm and could indicate potential sensor malfunctions, unusual patient conditions, or data transmission errors. Identifying these outliers is the first step in root-cause analysis and improving overall system reliability.

<br>

<p align="center">
  <img src="https://i.imgur.com/jSteg1G.png" alt="Anomaly Detection Scatter Plot" width="700"/>
  <br>
  <em>Figure 2: Anomaly detection results using the Isolation Forest algorithm. The red 'x' markers represent anomalous data points that warrant further investigation.</em>
</p>

<br>

### Data Visualizations

I created a series of visualizations to provide a clear and insightful overview of the sensor data.

#### Sensor Performance

To visualize the performance of different sensor types, I created a bar chart of the average efficiency ratio and a box plot of the performance score distribution.

<br>

<p align="center">
  <img src="https://i.imgur.com/hhKXPDd.png" alt="Average Efficiency Ratio by Sensor Type" width="700"/>
  <br>
  <em>Figure 3: Average efficiency ratio for each sensor type. A higher ratio indicates better performance, suggesting that ECG and PulseOximeter sensors are the most efficient in this dataset.</em>
</p>

<br>

<p align="center">
  <img src="https://i.imgur.com/IvY0FH1.png" alt="Performance Score Distribution by Sensor Type" width="700"/>
  <br>
  <em>Figure 4: Distribution of performance scores for each sensor type. The outliers in the BloodPressure sensor data suggest that while its median performance is good, it has a higher rate of exceptionally poor performance readings compared to other sensors.</em>
</p>

<br>

**Key Insights from the Visualizations:**

-   `ECG` and `PulseOximeter` sensors have the highest average efficiency.
-   The performance scores for all sensor types have a similar median, but some, like `BloodPressure`, have a wider range of outliers.

#### Correlation Matrix

This heatmap reveals the relationships between different sensor metrics, which is crucial for feature engineering and understanding the data.

- **Insight**: The strong positive correlation (0.87) between `bytes_per_duration` and `performance_score` confirms that a higher data transmission rate is a key driver of overall performance. Conversely, the strong negative correlation (-0.73) between `transmission_duration` and `bytes_per_duration` highlights the trade-off between transmission time and data rate.

<br>

<p align="center">
  <img src="https://i.imgur.com/S4G7iXc.png" alt="Correlation Matrix" width="600"/>
  <br>
  <em>Figure 5: Correlation matrix of key sensor performance metrics. This visualization helps to quickly identify key relationships and inform feature selection for future modeling.</em>
</p>

<br>

## Technologies Used

- **Palantir Foundry**: For building and deploying the production ETL pipeline.
- **Python**: For data analysis and machine learning.
- **Libraries**: pandas, scikit-learn, matplotlib, seaborn.

## Conclusion

This project demonstrates a full-cycle data workflow, from ETL pipeline construction to advanced machine learning analysis and visualization. It showcases a strong command of Palantir Foundry, data engineering principles, and data science techniques, making it a compelling demonstration of a full-cycle data project.

## References

[1] Kaggle. (2023). *IoT-Sensor-Data-for-Energy-Efficiency-in-Wireless-Body-Sensor-Networks*. Retrieved from https://www.kaggle.com/datasets/cde-paas/iotsensordataforenergyefficiencyinwirelessbodysensornetworks

[2] Liu, F. T., Ting, K. M., & Zhou, Z. H. (2008). Isolation Forest. *2008 Eighth IEEE International Conference on Data Mining*, 413-422.
