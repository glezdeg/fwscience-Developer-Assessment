# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

# connection method
def create_connection(config):
    try:
        print('Creating conection:{}'.format(config))
        cnx = mysql.connector.connect(**config)
        cursor=cnx.cursor()
        return cnx,cursor
    except Exception as e:
        print('Conection error:',e)
    

# database creation
def create_database(config,DB_NAME='companies'):
    #conection create
    cnx,cursor=create_connection(config)
    
    try:
        print('Creating {} database'.format(DB_NAME))
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8';".format(DB_NAME))
        print('OK')
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
    
    try:
        #comit changes
        cnx.commit()
        #cursor and conection close
        cursor.close()
        cnx.close()
    except Exception as e:
        print('Error closing conection:',e)


#table creation
def create_table(config,TB_NAME,TB_DESCRIPTION):
    #conection create
    cnx,cursor=create_connection(config)
    
    try:
        print("Creating table {}: ".format(TB_NAME))
        cursor.execute(TB_DESCRIPTION.format(TB_NAME))
        print('OK')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table {} already exists.".format(TB_NAME))
        else:
            print(err.msg)
    
    try:
        #comit changes
        cnx.commit()
        #cursor and conection close
        cursor.close()
        cnx.close()
    except Exception as e:
        print('Error closing conection:',e)

#data insertion
def insert_data(config,TABLE,INSERT_QUERY,INSERT_DATA):
    #conection create
    cnx,cursor=create_connection(config)
    
    try:
        print('Inserting company {}'.format(INSERT_DATA))
        cursor.execute(INSERT_QUERY.format(TABLE),INSERT_DATA)
        print('OK')
    except mysql.connector.Error as err:
        print(err.msg)
    except Exception as e:
        print('Error inserting data:',e)
        print('Error:',e)
    
    try:
        #comit changes
        cnx.commit()
        #cursor and conection close
        cursor.close()
        cnx.close()
    except Exception as e:
        print('Error closing conection:',e)

#data selection
def select_data(config,TABLE,SELECT_QUERY):
    #conection create
    cnx,cursor=create_connection(config)
    
    cursor.execute(SELECT_QUERY.format(TABLE))
    data=list(cursor)
    
    try:
        #cursor and conection close
        cursor.close()
        cnx.close()
    except Exception as e:
        print('Error closing conection:',e)

    
    return data

if __name__=='__main__':
    #database creation example
    config={
        'user':'root',
        'password':'diego353',
        'host':'127.0.0.1',
        }
    dbname='companies'
    create_database(config,DB_NAME=dbname)
    
    #table creation example
    dbname='companies'
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
        linkedin_url VARCHAR(255));
    '''
    create_table(config, TB_NAME=tbname, TB_DESCRIPTION=tbdescription)
    
    #insert data example
    dbname='companies'
    tbname='company'
    config={
        'user':'root',
        'password':'diego353',
        'host':'127.0.0.1',
        'database':dbname,
        }
    
    insert_company='''
    INSERT INTO {}
        (name,short_name,website_url,linkedin_url)
        VALUES (%s,%s,%s,%s);'''
    data_company=('Aliaswire','','http://www.aliaswire.com','')
    insert_data(config,
                TABLE=tbname,
                INSERT_QUERY=insert_company,
                INSERT_DATA=data_company)
    
    #select companies
    dbname='companies'
    tbname='company'
    config={
        'user':'root',
        'password':'diego353',
        'host':'127.0.0.1',
        'database':dbname,
        }
    company_query='SELECT * FROM {};'
    data=select_data(config,
                TABLE=tbname,
                SELECT_QUERY=company_query)
    print(data)
    