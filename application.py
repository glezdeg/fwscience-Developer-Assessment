# -*- coding: utf-8 -*-
import dbhandlers.mysqlhandler as mysql
from dbhandlers.duplicatehandler import report_duplicates
import os
import pandas as pd


#directories
current_dir = os.path.abspath(os.path.dirname(__file__)) 
data_dir=os.path.join(current_dir,'companies_example_data.csv')



#data from csv file reporting duplicates
def main_csv_report():
    DF=pd.read_csv(data_dir)
    report_duplicates(DF,'name',current_dir)


#data from mysql db reporting duplicates
def main_sql_report():
    data=generate_mysql_data_example()
    DF=pd.DataFrame(data)
    column_names=('Id','name','short_name','website_url','linkedin_url')
    DF.columns=column_names
    report_duplicates(DF,'name',current_dir)


#create data form csv to mysql
def generate_mysql_data_example():    
    # csv data to pandas dataframe
    DF=pd.read_csv(data_dir)
        
    #database creation
    config={
            'user':'root',
            'password':'diego353',
            'host':'127.0.0.1',
            }
    dbname='companies'
    mysql.create_database(config,DB_NAME=dbname)
    
    #table creation
    config={
            'user':'root',
            'password':'diego353',
            'host':'127.0.0.1',
            'database':dbname
            }
    tbname='company'
    tbdescription='''
        CREATE TABLE {} (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            short_name VARCHAR(50),
            website_url VARCHAR(255),
            linkedin_url VARCHAR(255)
        );
        '''
    mysql.create_table(config, TB_NAME=tbname, TB_DESCRIPTION=tbdescription)
        
    #insert data from csv to mysql to simulate database
    insert_company='''
    INSERT INTO {}
    (name,short_name,website_url,linkedin_url)
    VALUES (%s,%s,%s,%s);'''
    
    for i,row in DF.iterrows():
        data_company=(row['name'],
                      row['short_name'],
                      row['website_url'],
                      row['linkedin_url'])
                      
        mysql.insert_data(config,
                    TABLE=tbname,
                    INSERT_QUERY=insert_company,
                    INSERT_DATA=data_company)
        
    company_query='SELECT * FROM {};'
    data=mysql.select_data(config,
                    TABLE=tbname,
                    SELECT_QUERY=company_query)
    return data
    
    
if __name__=='__main__':
    main_csv_report()
     
    
    
