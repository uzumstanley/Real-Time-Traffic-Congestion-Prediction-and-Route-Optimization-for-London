# Collision Analysis Project

## Overview

This project aims to analyze TfL collision data to understand patterns, severity, and contributing factors. The dataset contains detailed information about various collisions, including time, location, vehicle types, and environmental conditions. The goal is to build a predictive model to assess collision severity and derive actionable insights.

## Dataset

The dataset consists of 208,665 entries with 36 columns. Key columns include:

- **X, Y**: Geographical coordinates
- **OBJECTID, COLLISION_REF**: Unique identifiers for each collision
- **VEHICLE_TYPE**: Type of vehicle involved
- **COLLISION_SEVERITY**: Severity of the collision
- **EASTING, NORTHING**: Coordinates in a different format
- **YEAR, COLLISION_DATE, TIME**: Temporal information
- **BOROUGH, HIGHWAY, LOCATION**: Location details
- **ROAD_SURFACE, LIGHT_CONDITIONS, WEATHER**: Environmental conditions
- **DRIVERS_AGE, DRIVERS_SEX**: Driver demographics
- **HIT_AND_RUN, SKIDDING**: Incident specifics
- **CASUALT_AGES, CASUALT_SEVERITIES**: Casualty information

Tech Stack Python and Tools/Libraries:

Python Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn.
## Data Preprocessing

1. **Handling Missing Values**: 
   - Columns like `DRIVERS_AGE`, `DRIVERS_SEX`, and `HIT_AND_RUN` have missing values that need to be addressed.
   - Imputation or removal strategies will be applied based on the context.

2. **Feature Engineering**:
   - Extract additional features from `COLLISION_DATE` and `TIME` such as day of the week, month, and hour of the day.
   - Encode categorical variables like `VEHICLE_TYPE`, `COLLISION_SEVERITY`, and `WEATHER` using appropriate techniques.

3. **Normalization and Scaling**:
   - Scale numerical features to ensure uniformity in the model.

## Model Building

### Model Selection

A classification model was chosen to predict the severity of collisions. The target variable is `COLLISION_SEVERITY`.

### Model Training

- The dataset was split into training and testing sets.
- A baseline model was trained to establish a performance benchmark.
- Various algorithms such as Logistic Regression, Random Forest, and Gradient Boosting were evaluated.

### Model Evaluation

- **Accuracy**: The model achieved an accuracy of approximately 85.97%.
- **Precision, Recall, F1-Score**:
  - For class 0: Precision 0.86, Recall 1.00, F1-Score 0.92
  - For class 1: Precision 0.00, Recall 0.00, F1-Score 0.00
- The model performs well for class 0 but struggles with class 1, indicating a need for further tuning or data balancing.

## Findings and Insights

### Temporal Patterns
- Collisions are more frequent during certain times of the day. The graph "Collisions by Time of Day" shows peaks during rush hours.

### Severity Distribution
- The distribution of collision severity is heavily skewed towards "Slight" collisions, with "Serious" and "Fatal" collisions being significantly less frequent. This is evident from the "Distribution of Collision Severity" graph.

### Geographical Insights
- Certain boroughs have higher collision rates. For example, Westminster has the highest number of collisions (6,924), followed by Lambeth (6305), Tower Hamlets (5,817) and Southwark (5,614). The "Collisions by Borough" table provides a detailed breakdown of collision counts by borough.

### Severity Factors
- Factors like road surface conditions, light conditions, and weather significantly impact collision severity.

## Future Work

- **Data Augmentation**: Collect more data to balance the classes and improve model performance.
- **Feature Importance**: Conduct a detailed analysis to identify the most influential features.
- **Model Tuning**: Experiment with hyperparameter tuning and advanced algorithms to enhance predictive accuracy.

## Conclusion

This project provides valuable insights into collision patterns and severity. The predictive model, despite its limitations, offers a foundation for further research and practical applications in traffic safety management. The analysis highlights key areas for intervention, such as improving road conditions in high-collision boroughs and enhancing safety measures during peak hours.

![Unknown-2](https://github.com/user-attachments/assets/5fa2af15-5a81-47a7-9b60-7d6dee9e7b8d)


![Unknown-2](https://github.com/user-attachments/assets/10b32f9e-8fb5-45ca-98a4-b9f893364a9e)

![Unknown-2](https://github.com/user-attachments/assets/49e83755-5769-4791-a272-2983d847f7ea)

