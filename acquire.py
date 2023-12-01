import env

def get_titanic_data():

    import env
    import os
    import pandas as pd
    """
    takes no arguements, acquires my titanic data from either a csv or sql 
    returns titanic dataframe
    """
    filename = 'titanic.csv'
    
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename, index_col=0) #wont make the index a new column
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        df = pd.read_sql('select * from passengers', url)

        #save to csv
        df.to_csv(filename)
        
    return df 


import os
def get_iris_data():

    import env
    import os
    import pandas as pd
    filename = 'iris.csv'
    
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename, index_col=0) #wont make the index a new column
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        df = pd.read_sql('select * from measurements join species using(species_id)', url)

        #save to csv
        df.to_csv(filename)
        
    return df 


def get_telco_data():
    import env
    import os
    import pandas as pd
    filename = 'telco.csv'
    
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename, index_col=0) #wont make the index a new column
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        df = pd.read_sql(
        '''
SELECT 
        customers.*,
        contract_types.contract_type,
        payment_types.payment_type,
        internet_service_types.internet_service_type
    FROM customers
    LEFT JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id
    LEFT JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id
    LEFT JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id;

'''
        , url)

        #save to csv
        df.to_csv(filename)
        
    return df 

