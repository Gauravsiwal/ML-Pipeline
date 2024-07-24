# ML-Pipeline
## This repository contains a complete end to end ML pipeline project

![image](https://github.com/user-attachments/assets/dc339d2d-4170-4a2b-b89e-bbde68c2550d)

The challenge at hand is frequent delays in truck routes causing significant financial losses in the logistics industry.
To address this issue, a machine learning pipeline has been developed, divided into three main phases: ETL (Extract,
Transform, Load), ML Modeling, and Deployment.

In the first phase, data is extracted from MySQL and PostgreSQL databases using Python connections. The extracted
data undergoes cleaning, engineering, and merging into a required dataset. This final dataset is then stored in
Hopsworks, which facilitates data storage, sharing, versioning, and analysis through its feature store.

Moving to the second phase, the dataset is loaded into a Jupyter notebook from Hopsworks for ML modeling. Here,
the data is pre-processed to handle missing values, outliers, and duplicate records. Features are encoded and
scaled to prepare them for modeling. Models like Logistic regression, Decision Tree, Random Forest and XGBoost
are fitted and validated on the dataset. The process includes leveraging Wandb (Weights and Biases) for model
registry, experimentation, tracking, and tuning. Ultimately, the best-performing model is selected for deployment.

In the final phase, the chosen model is deployed by creating a Streamlit application and hosting it on GitHub. This application
serves to predict the likelihood of truck delays based on the trained model's insights.
Application link: https://ml-pipeline-cqfgrtvduftttgkdkagfr6.streamlit.app/

Overall, this pipeline aims to empower logistics companies with predictive capabilities to mitigate delays and
associated financial losses effectively.

