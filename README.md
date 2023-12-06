# Project Overview and Goal:

- According to TechSee's report based on a 2019 survey result,39% of Americans canceled their telecom contracts due to unsatisfied customer service (TechSee Augmented Vision Ltd., 2022).

- Reactive retention strategies are shown to be ineffective, instead, proactive efforts are key.

- This project will invstigate why customers of Telco churn, with statistical analysis and model building.

- The goal is to develop a ML classification model in order to predict the churning pattern of a customer, and therefore implementing proactive measures to prevent the churning before it happens.

# Questions explored:
- How many customers have churned?
- How do monthly charges, total charges and tenure (continuous variables) affect churn?
- How are the categorical variables affect churn?
- Do people have higher tenure tend to have lower monthly charges?

# Data dictionary:

<img width="832" alt="Screenshot 2023-12-05 at 10 52 10 PM" src="https://github.com/kelseyhangyu/Telcos_Customer_Churn_Drivers/assets/146888019/bdba72eb-b18b-48b6-a5ec-ba1058d9a12b">


# Project planning
- Data acquisition from mysql with credentials
- Data preparation:
  > removed duplicated columns
  > fill NaN values in internet_service_type column and churn_month column
  > fill the ' ' in total_charges column with 0 and convert it to float
  > drop the 3 id columns
  > split the dataset into train, validate and test for future modeling
- Data Exploration:
  > Answer the above proposed 4 questions with visualizations and statistical tests
- Modeling:
  > Used decision tree, random forest and knn
- Delivery
  > Draw conclusions
  > Present findings

# Reproduction of findings
- request credential for mysql server from Codeup
- clone this repository

# Key Findings
- Random forest model(n_estimators=700, max_depth=4) is chosen to be the best model, with 79% accuracy
- The chosen model is conservative on prediction compared to actual values
- No churn: lower monthly charges, higher tenure, no Internet service, 2-year contract, no paperless billing and credit card payment
  > Recommendations:
     - encourage 2-year contract, no papperless billing and credit card auto payment through various stimulations
     - lower monthly charges
  > Next Steps:
  - To quantify how much each controllable factor can affect churning status, especially on internet service
