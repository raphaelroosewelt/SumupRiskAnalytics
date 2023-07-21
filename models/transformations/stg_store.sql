-- transformations/transform_staging_store.sql
-- Clean and standardize the "ADDRESS" column
with
    standardized_store as (
        select
            id,
            name,
            trim(upper(address)) as address,  -- Convert to uppercase and remove leading/trailing spaces
            city,
            country,
            created_at,
            typology,
            customer_id
        from {{ ref("staging_store") }}  -- Reference the "staging_store" table
    )

    -- Insert the transformed data into the "staging_store_temp" table
    insert into {{ target("staging_store_temp") }}
select *
from standardized_store
;