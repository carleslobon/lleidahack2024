# Project Title: Predictive Model for Process Data

## Overview

This project aims to build a predictive model for process data, using machine learning techniques to predict outcomes based on historical session data. We focused on delivering a high-quality solution to address a specific challenge by leveraging state-of-the-art models, data preprocessing techniques, and exploring alternative solutions to enhance the model's accuracy and performance.

## Table of Contents

1. [Why We Made These Decisions](#why-we-made-these-decisions)
2. [Preprocessing](#preprocessing)
3. [Models](#models)
4. [Other Solutions](#other-solutions)
5. [Conclusions](#conclusions)
6. [Meet the Team](#meet-the-team)

## Why We Made These Decisions

In this project, we made several key decisions to ensure the delivery of a high-quality solution. Our goal was to create a model that would provide accurate and efficient predictions while remaining performant. Below are the key factors that guided our decisions:

- Prioritized cleaning and preprocessing the dataset to ensure high-quality data.
- Selected a combination of pre-trained models and custom fine-tuned solutions for optimal performance.
- Explored alternative approaches like clustering techniques, RNNs, and GNNs to enhance model capabilities.

## Preprocessing

Data preprocessing was a critical step in ensuring the quality of the input data for our models. The following steps were taken during preprocessing:

- **Removing invalid rows**: We removed rows where the process was not valid.
- **Grouping by sessions**: Data was grouped by sessions, which allowed us to establish a meaningful, sequential order.
- **Reducing consecutive rows**: We reduced the number of consecutive rows with identical session, action, and process features to just one.
- **Deleting irrelevant rows**: Rows with only one process per session were deleted, as they didn’t provide useful information for the model.

These preprocessing steps helped ensure that the data fed into the model was clean and of high quality.

## Models

For the predictive model, we aimed for both accuracy and efficiency. The model selection process included the following steps:

- **LSTM (Long Short-Term Memory)**: We chose an LSTM model to predict the results due to the sequential nature of the data and its ability to capture temporal dependencies and patterns.
- **Hyperparameter tuning**: We adjusted important hyperparameters like learning rate and batch size to maximize model performance.
- **Performance considerations**: Our approach balanced accuracy and efficiency to deliver reliable predictions without compromising computational efficiency.

## Other Solutions

In addition to machine learning models, we explored other potential solutions to improve the user experience and prediction accuracy:

- **Data Augmentation**: Techniques were considered to improve the generalization ability of the model.
- **Hybrid Approaches**: We explored combining machine learning with rule-based systems to enhance prediction accuracy.
- **Cloud Services**: We evaluated the use of cloud services to scale the system and handle large datasets efficiently.
- **Ensemble Methods**: Implementing ensemble methods was considered to combine predictions from multiple models for improved performance.
- **Clustering Techniques**: We explored clustering algorithms such as DBSCAN and K-Nearest Neighbors (KNN) to identify patterns in the data and group similar processes.
- **Advanced RNNs**: We tested more advanced Recurrent Neural Networks (RNNs), such as Transformers, to capture complex relationships in sequential data.
- **Graph Neural Networks (GNNs)**: We explored GNNs to model relationships between processes as a graph structure.

While we decided to prioritize machine learning models for the core of our solution, we continue to explore these additional techniques to improve model performance in the future.

## Conclusions

In conclusion, the decisions made throughout the development of this project were designed to ensure the best user experience and model performance. By focusing on clean data, efficient models, and continuous exploration of other solutions, we are confident that our approach will deliver the results our users need. We are excited about the potential of this solution and will continue to refine it as we gather more insights and feedback.

## Meet the Team

We are a dedicated team of students who worked collaboratively to bring this project to life. Below, you can find our LinkedIn profiles to learn more about us:

- [Gerard Gispert](https://www.linkedin.com/in/gerard-gispert-carreras-34b290265/) - Software student at UPC
- [Carles Lobon](https://www.linkedin.com/in/carles-lobon-quilez-715149275/) - Software student at UPC

Feel free to connect with us on LinkedIn to discuss our project or collaborate on future opportunities!

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
