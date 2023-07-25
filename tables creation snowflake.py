#!/usr/bin/env python
# coding: utf-8

# # ELT Pipeline 

# ### Autor: Raphael Roosewelt | Date: 19.07.2023 | Last modifications: 24.07.2023

# #### Importing packages

# In[ ]:


#Assuming all packages were previously downloaded.
import pandas as pd
import snowflake.connector
import dbtimport subprocess
import os
from dbt.clients import system


# #### Estabilishing Connection with DWH - Sonwflake.

# In[ ]:


# Defining Snowflake connection configuration
snowflake_config = {
    "user": "ROOSEWELT2020",
    "password": "#TestSumUp2020",
    "account": "dvihgoi-yg27269",
    "warehouse": "COMPUTE_WH",
    "database": "CUSTOMER_TARGETING",
    "schema": "PUBLIC"
}


# In[ ]:


# Connecting to Snowflake
conn = snowflake.connector.connect(user=snowflake_config['user'],
                                   password=snowflake_config['password'],
                                   account=snowflake_config['account'],
                                   warehouse=snowflake_config['warehouse'],
                                   database=snowflake_config['database'],
                                   schema=snowflake_config['schema'])


# In[ ]:


# Creating a cursor.
cursor = conn.cursor()


# # Creating tables on Snowflake

# ### a.Table staging_device

# In[ ]:


# Creating table staging_device.
create_table_query = "CREATE OR REPLACE TABLE staging_device(ID NUMBER(38,0), TYPE NUMBER(38,0),STORE_ID NUMBER(38,0))"
cursor.execute(create_table_query)


# In[ ]:


# File path to the CSV file
csv_file_path = (r'C:\Users\Asus\Desktop\sumup_data\device.csv')


# In[ ]:


# Reading device.csv
df = pd.read_csv(r'C:\Users\Asus\Desktop\sumup_data\device.csv',parse_dates=True)


# In[ ]:


# Loading data into staging_device
insert_query = "INSERT INTO staging_device (id, type, store_id) VALUES (%s, %s, %s)"


# In[ ]:


# Loading data into staging_device table using a DataFrame
cursor.executemany(insert_query, df.values.tolist())


# #### Checking the data loaded into table "staging_device" 

# In[ ]:


query = "SELECT * FROM staging_device LIMIT 10"
cursor.execute(query)


# In[ ]:


# Fetching column headers
column_headers = [desc[0] for desc in cursor.description]


# In[ ]:


# Fetching the rows
rows = cursor.fetchall()


# In[ ]:


# Convert the data to a pandas DataFrame
df = pd.DataFrame(rows, columns=column_headers)


# In[ ]:


print(df)


# ### b.Table staging_store

# In[ ]:


# Creating table staging_store.
create_table_query = """CREATE OR REPLACE TABLE staging_store (
        ID NUMBER(38,0), NAME VARCHAR(100), ADDRESS VARCHAR(100), CITY VARCHAR(100),
        COUNTRY VARCHAR(100), CREATED_AT TIMESTAMP_NTZ(9), TYPOLOGY VARCHAR(100), CUSTOMER_ID NUMBER(38,0))"""


# In[ ]:


cursor.execute(create_table_query)


# In[ ]:


# File path to the CSV file
csv_file_path = (r'C:\Users\Asus\Desktop\sumup_data\store.csv')


# In[ ]:


# Reading device.csv
df = pd.read_csv(r'C:\Users\Asus\Desktop\sumup_data\store.csv',parse_dates=True)


# In[ ]:


# Loading data into staging_store
insert_query = 
    """INSERT INTO staging_store (
            ID, NAME, ADDRESS, CITY, COUNTRY, CREATED_AT, TYPOLOGY, CUSTOMER_ID) 
        VALUES (%s, %s, %s, %s, %s, %s,%s,%s)
    """


# In[ ]:


# Loading data into staging_store table using a DataFrame
cursor.executemany(insert_query, df.values.tolist())


# #### Checking the data loaded into table "staging_store" 

# In[ ]:


query = "SELECT * FROM staging_store LIMIT 10"
cursor.execute(query)


# In[ ]:


# Fetching column headers
column_headers = [desc[0] for desc in cursor.description]


# In[ ]:


# Fetching the rows
rows = cursor.fetchall()


# In[ ]:


# Convert the data to a pandas DataFrame
df = pd.DataFrame(rows, columns=column_headers)


# In[ ]:


print(df)


# ### b.Table staging_transaction

# In[ ]:


# Creating table staging_transaction.
create_table_query = """
    CREATE OR REPLACE TABLE staging_transaction (
        ID NUMBER(38,0),
        DEVICE_ID NUMBER(38,0),
        PRODUCT_NAME VARCHAR(100),
        PRODUCT_SKU VARCHAR(100),
        CATEGORY_NAME VARCHAR(100),
        AMOUNT NUMBER(10,2),
        STATUS VARCHAR(20),
        CARD_NUMBER VARCHAR(100),
        CVV NUMBER(38,0),
        CREATED_AT TIMESTAMP_NTZ(9),
        OCCUR_AT TIMESTAMP_NTZ(9)
    )
"""


# In[ ]:


# Executing the SQL command to create the table.
cursor.execute(create_table_query)


# In[ ]:


# File path to the CSV file
csv_file_path = (r'C:\Users\Asus\Desktop\sumup_data\transaction.csv')


# In[ ]:


# Reading transaction.csv
df = pd.read_csv(r'C:\Users\Asus\Desktop\sumup_data\transaction.csv',parse_dates=True)


# In[ ]:


# Preparing the INSERT query
insert_query = 
""" 
    INSERT INTO staging_transaction (
        ID, 
        DEVICE_ID, 
        PRODUCT_NAME, 
        PRODUCT_SKU, 
        CATEGORY_NAME, 
        AMOUNT, STATUS, 
        CARD_NUMBER, 
        CVV, CREATED_AT, 
        OCCUR_AT)
    VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# In[ ]:


# Loading data into staging_transaction table using a DataFrame
cursor.executemany(insert_query, df.values.tolist())


# #### Checking dataset loaded into table "staging_transaction" 

# In[ ]:


query = "SELECT * FROM staging_transaction LIMIT 10"
cursor.execute(query)


# In[ ]:


# Fetching column headers
column_headers = [desc[0] for desc in cursor.description]


# In[ ]:


# Fetching the rows
rows = cursor.fetchall()


# In[ ]:


# Convert the data to a pandas DataFrame
df = pd.DataFrame(rows, columns=column_headers)


# In[ ]:


print(df)


# In[ ]:


# Commiting the changes.
conn.commit()
# conn.close()


# ### D.Table customer_targeting

# In[ ]:


# Creating table customer_targeting.
create_table_query = """
    CREATE OR REPLACE TABLE customer_targeting (
        STORE_ID VARCHAR(100),
        NAME VARCHAR(100),
        ADDRESS VARCHAR(100),
        CITY VARCHAR(100),
        COUNTRY VARCHAR(100),
        CREATED_AT_TRANSACTION TIMESTAMP_NTZ(9),
        TYPOLOGY VARCHAR(100),
        CUSTOMER_ID VARCHAR(100),
        TYPE VARCHAR(100),
        TRANSACTION_ID VARCHAR(100),
        DEVICE_ID VARCHAR(100),
        PRODUCT_NAME VARCHAR(100),
        PRODUCT_SKU VARCHAR(100),
        CATEGORY_NAME VARCHAR(100),
        AMOUNT NUMBER(10, 2),
        STATUS VARCHAR(20),
        CARD_NUMBER VARCHAR(100),
        CVV VARCHAR(100),
        CREATED_AT TIMESTAMP_NTZ(9),
        OCCUR_AT TIMESTAMP_NTZ(9)
    )
"""


# In[ ]:


# Executing the SQL command to create the table.
cursor.execute(create_table_query)


# In[ ]:


# Generating the insert query
insert_query = """
    INSERT INTO customer_targeting (
        STORE_ID,
        NAME,
        ADDRESS,
        CITY,
        COUNTRY,
        CREATED_AT_TRANSACTION,
        TYPOLOGY,
        CUSTOMER_ID,
        TYPE,
        TRANSACTION_ID,
        DEVICE_ID,
        PRODUCT_NAME,
        PRODUCT_SKU,
        CATEGORY_NAME,
        AMOUNT,
        STATUS,
        CARD_NUMBER,
        CVV,
        CREATED_AT,
        OCCUR_AT
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    )
"""


# In[ ]:


# Executing the SQL command to create the table.
cursor.execute(create_table_query)


# In[ ]:


# Fetching column headers
column_headers = [desc[0] for desc in cursor.description]


# In[ ]:


# Fetching the rows
rows = cursor.fetchall()


# In[ ]:


# Convert the data to a pandas DataFrame
df = pd.DataFrame(rows, columns=column_headers)


# In[ ]:


print(df)


# ### Loading final data into table customer_targeting.

# In[ ]:


path_profiles = (r'C:\Users\Asus\Desktop\my_dbt_projects\dbt_projects\sumup_dt_task\models')


# In[ ]:


dbt_command = f"dbt run --profiles-dir {path_profiles}"


# In[ ]:


result = subprocess.run(dbt_command, shell=True, capture_output=True, text=True)


# In[ ]:


print(result.stdout)

