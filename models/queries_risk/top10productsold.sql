select product_name, count(*) as total_sold
from prd_risk_analytics.public.view_customer_targeting
group by product_name
order by total_sold desc
limit 10
;
