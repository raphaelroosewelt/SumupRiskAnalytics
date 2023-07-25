select typology, country, avg(amount) as avg_transacted_amount
from prd_risk_analytics.public.view_customer_targeting
group by typology, country
;