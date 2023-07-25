select
    type,
    count(*) as transaction_count,
    100.0
    * count(*)
    / (
        select count(*) from prd_risk_analytics.public.view_customer_targeting
    ) as percentage_of_transactions
from prd_risk_analytics.public.view_customer_targeting
group by type
;
