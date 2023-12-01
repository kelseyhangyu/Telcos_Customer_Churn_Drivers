import env


def get_telco_data():
    import env
    import os
    import pandas as pd
    filename = 'telco_raw.csv'
    
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        telco = pd.read_csv(filename, index_col=0) #wont make the index a new column
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        telco = pd.read_sql(
        '''
SELECT *
FROM customers
LEFT JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id
LEFT JOIN customer_churn ON customers.customer_id = customer_churn.customer_id
LEFT JOIN customer_contracts ON customers.customer_id = customer_contracts.customer_id
LEFT JOIN customer_details ON customers.customer_id = customer_details.customer_id
LEFT JOIN customer_payments ON customers.customer_id = customer_payments.customer_id
LEFT JOIN customer_signups ON customers.customer_id = customer_signups.customer_id
LEFT JOIN customer_subscriptions ON customers.customer_id = customer_subscriptions.customer_id
LEFT JOIN internet_service_types ON customer_subscriptions.internet_service_type_id = internet_service_types.internet_service_type_id
LEFT JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id
'''
        , env.get_db_url('telco_churn', user=env.user, password=env.password, host=env.host))

        #save to csv
        telco.to_csv(filename)
        
    return telco