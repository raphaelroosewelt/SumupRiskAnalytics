select 
to_varchar(id) as id,
to_varchar(device_id) as device_id,
upper(trim(regexp_replace((product_name), '[.#,]', ''))) as product_name,


to_varchar(floor(cast(regexp_replace(product_sku, '[vV]', '') as numeric))) as product_sku,
upper(trim(regexp_replace((category_name), '[.#,]', ''))) as category_name,
amount as amount,
upper(trim(status)) as status,
to_varchar(lpad(cast(regexp_replace(card_number, ' ', '') AS BIGINT), 19, '0')) AS card_number,
to_varchar(cvv) as cvv,

created_at,
occur_at
from staging_transaction a