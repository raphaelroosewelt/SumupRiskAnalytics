# Sumup RiskAnalytics Technical Test

Key findings
---------------------------------------------------------------------------
- On average, a store makes its 5 first transactions in 44 days;
- Regarding Tipology, "Florist" takes the first position with €509 in average sales and "Foodtruck" the least with €476;
- The most used device is type 4 with 23,3% although no big difference was perceived among otters;
- Colombia is the country with the biggest ticket on average: €737.

  ![image](https://github.com/raphaelroosewelt/SumupRiskAnalytics/assets/140111797/66ee8c78-1bfd-41e9-abdb-7474ca081aef)


Executive Summary:
--------------------------------------------------------------------------
Snowflake was chosen as Cloud Data Warehouse to store tables. Data were transformed using dbt cloud, as well as ingested into staging tables and the target table. Jupyter Notebook was used for table creation. To load data into the target table, dbt was integrated with Jupyter. 

Finally, Tableau was employed to create a Dashboard, making it easier for stakeholders to interact with the transformed information. Is worth mentioning that Python and SQL were the languages selected for the test.

Two out of three files presented real challenges regarding data quality, such as non-standardized fields like "card_number." Others contained numeric characters that would not be used in calculations. 

The adopted solution was to standardize all three files beforehand, ensuring the cleansing of the entire dataset. The SQL queries inside the "transformations" tab document the steps taken. 

Implementation Approach:
---------------------------------------------------------------------------
As three files were received, the adopted solution was the creation of a flat table that got  data from three staging tables. Afterwards, a view table was generated. By adopting this solution, we can assure a single source of truth, ensure data quality, and guarantee process governance. In terms of the volume of data, my assumption is, since this is a simple solution, we could avoid issues regarding updates and maintenance. 

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
