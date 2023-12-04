import pandas as pd
import numpy as np
def prep_telco(telco):
    '''
    fill NaN values in internet_service_type column and churn_month column
    fill the ' ' in total_charges column with 0 and convert it to float
    drop the id columns
    '''
    telco['internet_service_type']=telco['internet_service_type'].fillna('No internet service')
    telco['churn_month']=telco['churn_month'].fillna('not churned')
    telco.total_charges = telco.total_charges.replace(' ','0.0')
    telco.total_charges = telco.total_charges.astype(float)
    telco=telco.drop(['payment_type_id'],axis =1)
    telco=telco.drop(['contract_type_id'],axis =1)
    telco=telco.drop(['internet_service_type_id'],axis =1)
    return telco



from sklearn.model_selection import train_test_split
def split(df,target_variable):
    '''
    split the dataframe into 3 subsets with 60%, 20% and 20% ratio
    
    '''

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
