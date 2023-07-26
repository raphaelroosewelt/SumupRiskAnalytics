# Sumup RiskAnalytics Technical Test

Key findings
---------------------------------------------------------------------------
- On average, a store makes its 5 first transactions in 44 days;
- Regarding Tipology, "Florist" takes the first position with €509 in average sales and "Foodtruck" the least with €476;
- The most used device is type 4 with 23,3% although no big difference was perceived among otters;
- Colombia is the country with the biggest ticket on average: €737.
  
![image](https://github.com/raphaelroosewelt/SumupRiskAnalytics/assets/140111797/c7517f45-9a92-415c-a697-0025534f750d)

Executive Summary:
--------------------------------------------------------------------------
Snowflake was chosen as Cloud Data Warehouse to store tables. Data were transformed using dbt cloud, as well as ingested into staging tables and the target table. Jupyter Notebook was used for table creation. To load data into the target table, dbt was integrated with Jupyter. 

Finally, Tableau was employed to create a Dashboard, making it easier for stakeholders to interact with the transformed information. Is worth mentioning that Python and SQL were the languages selected for the test.

Two out of three files presented real challenges regarding data quality, such as non-standardized fields like "card_number." Others contained numeric characters that would not be used in calculations. 

The adopted solution was to standardize all three files beforehand, ensuring the cleansing of the entire dataset. The SQL queries inside the "transformations" tab document the steps taken.

![architecture-data-sumup-riskan-alytics](https://github.com/raphaelroosewelt/SumupRiskAnalytics/assets/140111797/2dd22402-d230-4037-b971-7c3787dda1c8)

Implementation Approach:
---------------------------------------------------------------------------
The adopted solution was the creation of a flat table from three staging tables, as shown below: 
![image](https://github.com/raphaelroosewelt/SumupRiskAnalytics/assets/140111797/ca94e1f2-598c-4900-8ff2-219a34c4f8da)

Summary of Table Relationships:
---------------------------------------------------------------------------
1. staging_transaction
Contains information about transactions with attributes such as "id," "device_id," "product_name," "product_sku," "category_name," "amount," "status," "card_number," "cvv," "created_at," and "occur_at."

2. staging_store
Stores information about stores with attributes like "store_id," "name," "address," "city," "country," "created_at," "typology," and "customer_id."

3. staging_device
Holds details about devices with attributes like "id," "type," and a foreign key "store_id" referencing "store_id" in the "staging_store" table.

4. store_device
An associative table representing the many-to-many relationship between "staging_store" and "staging_device." It has foreign keys "store_id" and "id," referencing "store_id" in the "staging_store" table and "id" in the "staging_device" table, respectively.

5. customer_targeting
Combines all attributes from the three previous tables. Includes attributes such as "store_id," "name," "address," "city," "country," "created_at_transaction," "typology," "customer_id," "type," "transaction_id," "device_id," "product_name," "product_sku," "category_name," "amount," "status," "card_number," "cvv," "created_at," and "occur_at."

Afterwards, a view table was generated. By adopting this solution, we can assure a single source of truth, ensure data quality, and guarantee process governance. In terms of the volume of data, my assumption is, since this is a simple solution, we could avoid issues regarding updates and maintenance. 

The final table:
![customer-targeting](https://github.com/raphaelroosewelt/SumupRiskAnalytics/assets/140111797/545d37e1-2ff9-44b8-90a4-63e69f5660c8)

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
