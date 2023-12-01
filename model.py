import pandas as pd


def preprocess_titanic(train,validate,test):
    dummy_train = pd.get_dummies(train[['sex','embark_town']], dummy_na=False, drop_first=[True, True]).astype(int)
    dummy_val = pd.get_dummies(validate[['sex','embark_town']], dummy_na=False, drop_first=[True, True]).astype(int)
    dummy_test = pd.get_dummies(test[['sex','embark_town']], dummy_na=False, drop_first=[True, True]).astype(int)

# Concatenate the dummy_df dataframe above with the original df.
    train = pd.concat([train, dummy_train], axis=1)
    validate = pd.concat([validate, dummy_val], axis=1)
    test = pd.concat([test, dummy_test], axis=1)

# Drop string values that have been replaced with encoded values.
    train = train.drop(columns=['sex', 'embark_town'])
    validate = validate.drop(columns=['sex', 'embark_town'])
    test = test.drop(columns=['sex', 'embark_town'])
    
    return train,validate,test

def preprocess_telco(train,validate,test):
    train['gender'] = train['gender'].replace({'Male':0,'Female':1})
    train['partner'] = train['partner'].map({'Yes':1,'No':0})
    dummy_train = pd.get_dummies(train[['contract_type','payment_type','internet_service_type','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn']], dummy_na=False, drop_first=[True, True]).astype(int)
    train = pd.concat([train, dummy_train], axis=1)
    train = train.drop(columns=['contract_type','payment_type','internet_service_type','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn'])

    validate['gender'] = validate['gender'].replace({'Male':0,'Female':1})
    validate['partner'] = validate['partner'].map({'Yes':1,'No':0})
    dummy_validate = pd.get_dummies(validate[['contract_type','payment_type','internet_service_type','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn']], dummy_na=False, drop_first=[True, True]).astype(int)
    validate = pd.concat([validate, dummy_validate], axis=1)
    validate = validate.drop(columns=['contract_type','payment_type','internet_service_type','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn'])

    test['gender'] = test['gender'].replace({'Male':0,'Female':1})
    test['partner'] = test['partner'].map({'Yes':1,'No':0})
    dummy_test = pd.get_dummies(test[['contract_type','payment_type','internet_service_type','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn']], dummy_na=False, drop_first=[True, True]).astype(int)
    test = pd.concat([test, dummy_test], axis=1)
    test = test.drop(columns=['contract_type','payment_type','internet_service_type','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn'])

    return train,validate,test
