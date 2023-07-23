with
    tb_step1 as (
        select
            -- to_varchar(lpad(id, 2, '0')) as store_id,
            to_varchar(id) as store_id,
            upper(trim(replace((name), '.', ''))) as name,

            upper(
                trim(
                    case
                        when address like '%St.%'
                        then regexp_replace((address), 'St\.', 'Street')

                        when address like '%Av.%'
                        then regexp_replace((address), 'Av.', 'Avenue')

                        when address like '%Ave%'
                        then regexp_replace(address, '\\bAve\\b', 'Avenue')

                        when address like '%Rd.%'
                        then regexp_replace((address), 'Rd.', 'Road')

                        else address
                    end
                )
            ) as address,

            trim(upper((city))) as city,
            trim(upper(country)) as country,
            created_at,
            trim(upper(typology)) as typology,
            to_varchar(customer_id) as customer_id

        from staging_store
    )

select
    store_id,
    name,
    regexp_replace((address), '[.#,]', '') as address,
    city,
    country,
    created_at,
    typology,
    customer_id

from tb_step1
;
