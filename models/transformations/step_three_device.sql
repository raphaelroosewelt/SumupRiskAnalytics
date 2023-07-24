select to_varchar(id) as id, to_varchar(type) as type, to_varchar(store_id) as store_id

from staging_device
limit 10
;
