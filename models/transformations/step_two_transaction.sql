-- transformations/transform_staging_store.sql
-- Clean and standardize the "ADDRESS" column
WITH standardized_store AS (
  SELECT
    ID,
    NAME,
    TRIM(UPPER(ADDRESS)) AS ADDRESS, -- Convert to uppercase and remove leading/trailing spaces
    CITY,
    COUNTRY,
    CREATED_AT,
    TYPOLOGY,
    CUSTOMER_ID
  FROM {{ ref('staging_store') }} -- Reference the "staging_store" table
)

-- Insert the transformed data into the "staging_store_temp" table
INSERT INTO {{ target('staging_store_temp') }}
SELECT * FROM standardized_store;