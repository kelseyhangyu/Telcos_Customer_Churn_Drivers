import pandas as pd
import numpy as np

def prep_iris(iris):
    iris = iris.reset_index(drop=True)
    iris = iris.drop(['measurement_id'], axis=1)
    iris = iris.rename(columns={'species_name':'species'})
    return iris

def prep_titanic(titanic):
    titanic = titanic.drop(['class'], axis=1)
    titanic = titanic.drop(['embarked'], axis=1)
    titanic['age'] = titanic['age'].fillna(titanic.age.mean())
    titanic['embark_town'] = titanic['embark_town'].fillna(titanic.embark_town.mode()[0])
    titanic = titanic.drop(columns=['deck'])
    return titanic

def prep_telco(telco):
    telco= telco.drop(['payment_type_id'],axis =1)
    telco=telco.drop(['contract_type_id'],axis =1)
    telco=telco.drop(['internet_service_type_id'],axis =1)
 # Strip leading and trailing whitespaces from the column with blank values
    telco['total_charges'] = telco['total_charges'].str.strip()
# Drop rows with blank values in the specified column
    telco = telco[telco['total_charges'] != '']
    telco['internet_service_type'] = telco['internet_service_type'].fillna('neither')
    return telco


from sklearn.model_selection import train_test_split
def split(df,target_variable):

    #first split
    train, validate_test = train_test_split(df, 
                 train_size=0.60, #size of the train df, and the test size will default to 1-train_size
                random_state=123, #set any number here for consistency
                 stratify=df[target_variable] #need to stratify on target variable
                )
    
    #second split
    validate, test = train_test_split(validate_test, #this is the df that we are splitting now
                test_size=0.50, #set test or train size to 50%
                 random_state=123, #gotta send in a random seed
                stratify=validate_test[target_variable]#still got to stratify
                )
    
    return train, validate, test

