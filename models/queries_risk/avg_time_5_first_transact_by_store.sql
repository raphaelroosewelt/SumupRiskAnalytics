with
    ranked_transactions as (
        select
            store_id,
            name,
            transaction_id,
            created_at,
            row_number() over (
                partition by store_id order by created_at
            ) as transaction_number
        from prd_risk_analytics.public.view_customer_targeting
    ),
    first_five_transactions as (
        select store_id, name, created_at
        from ranked_transactions
        where transaction_number <= 5
    )
select
    store_id,
    name,
    datediff(day, min(created_at), max(created_at)) as delta_5_first_transact,
    round(avg(datediff(day, min(created_at), max(created_at))) over (), 1) as avgtime,
    round(
        stddev_pop(datediff(day, min(created_at), max(created_at))) over (), 0
    ) as devpad
from first_five_transactions
group by store_id, name
;