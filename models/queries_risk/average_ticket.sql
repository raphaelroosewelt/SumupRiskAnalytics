select store_id, name, sum(amount) as total_transacted_amount
from prd_risk_analytics.public.view_customer_targeting
group by store_id, name
order by total_transacted_amount desc
limit 10
;