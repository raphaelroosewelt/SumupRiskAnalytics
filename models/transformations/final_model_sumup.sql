with
    trns_staging_store as (
        select
            --to_varchar(lpad(id, 2, '0')) as store_id,
            to_varchar(id) as store_id,
    		upper(trim(replace((name), '.', ''))) as name,
            
            upper(trim(
            	case
                when address like '%St.%'
                then regexp_replace((address), 'St\.', 'Street')

                when address like '%Av.%'
                then regexp_replace((address), 'Av.', 'Avenue')

                when address like '%Ave%'
                then regexp_replace(address, '\\bAve\\b', 'Avenue')

                when address like '%Rd.%'
                then regexp_replace((address), 'Rd.', 'Road')

                when address = '  '
                then regexp_replace((address), '  ', ' ')

                else address
            end)) as address,

            trim(upper((city))) as city,
    		trim(upper(country)) as country,
    		created_at as created_at_transaction,
    		trim(upper(typology)) as typology,
    		to_varchar(customer_id) as customer_id
    
        from staging_store
    )

select
c.store_id,
name,
regexp_replace((address), '[.#,]', '') as address,
city,
country,
c.created_at_transaction,
typology,
customer_id,
--End First part: data from staging_store

--to_varchar(b.store_id) as store_id_tb_device,
to_varchar(b.type) as type,
-- End Second part: data from staging_device

to_varchar(a.id) as transaction_id,
to_varchar(a.device_id) as device_id,
upper(trim(regexp_replace((product_name), '[.#,]', ''))) as product_name,
to_varchar(floor(cast(regexp_replace(product_sku, '[vV]', '') as numeric))) as product_sku,
upper(trim(regexp_replace((category_name), '[.#,]', ''))) as category_name,
amount as amount,
upper(trim(status)) as status,
to_varchar(lpad(cast(regexp_replace(card_number, ' ', '') AS BIGINT), 19, '0')) AS card_number,
to_varchar(cvv) as cvv,
a.created_at created_at,
occur_at
--End Third part: data from staging_transaction

from staging_transaction a
left join staging_device b on a.device_id =b.id
left join trns_staging_store c on b.store_id = c.store_id

group by

c.store_id,
name,
address,
city,
country,
c.created_at_transaction,
typology,
customer_id,

--store_id_tb_device,
type,

transaction_id,
device_id,
product_name,
product_sku,
category_name,
amount,
status,
card_number,
cvv,
created_at,
occur_at

order by c.created_at_transaction asc;