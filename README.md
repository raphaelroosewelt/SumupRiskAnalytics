# Sumup RiskAnalytics Technical Test
Executive Summary:
--------------------------------------------------------------------------
I chose Snowflake as the Cloud Data Warehouse to create and store tables. Data were transformed using Dbt for ingestion into staging tables and the target table. Jupyter Notebook was used for table creation and data insertion into the target table. 

Finally, Tableau was employed to create a Dashboard, making it easier for stakeholders to interact with the transformed information. Is worth mentioning that Python and SQL were the languages selected for the test.

Two out of three files presented real challenges regarding data quality, such as non-standardized fields like "card_number." Others contained numeric characters that would not be used in calculations. 

The adopted solution was to standardize all three files beforehand, ensuring the cleansing of the entire dataset. The SQL queries inside the "transformations" tab document the steps taken. 

Implementation Approach:
---------------------------------------------------------------------------
As three files were received, the adopted solution was the creation of a flat table that obtained data from three staging tables. Afterwards, a wiel was generated. By adopting this solution, we can assure a single source of truth, ensure data quality, and guarantee process governance.

The final table has the following fields:
- STORE_ID,
- NAME,
- ADDRESS,
- CITY,
- COUNTRY,
- CREATED_AT_TRANSACTION,
- TYPOLOGY,
- CUSTOMER_ID,
- TYPE,
- TRANSACTION_ID,
- DEVICE_ID,
- PRODUCT_NAME,
- PRODUCT_SKU,
- CATEGORY_NAME,
- AMOUNT,
- STATUS,
- CARD_NUMBER,
- CVV,
- CREATED_AT,
- OCCUR_AT

Regarding  data trustworthiness and Controlled Model Changes
---------------------------------------------------------------------------
To ensure controlled model changes and data trustworthiness for stakeholders and consumers, we could follow the following points:

Controlled Model Changes:
- Version control, like Git, to track any changes we may have in key points such as code, data, and model configurations;
- A documentation routine for each model, reinforcing purpose, assumptions, and limitations;
- Implementing a staging layer for testing changes before production;
- Rollback plans;
- Effective communication and collaboration with key stakeholders and teams;

Assuring Data Trustworthiness:
- Data Quality check for missing values, outliers, and inconsistencies based on business requirements;
- Data documentation for origin and lineage transparency;
- Data validation for accuracy and anomaly detection;
- Transparency and explainability of data processing/modelling techniques;
