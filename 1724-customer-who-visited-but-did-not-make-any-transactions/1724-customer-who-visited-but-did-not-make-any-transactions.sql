# Write your MySQL query statement below
select customer_id,count(customer_id) as count_no_trans
from Visits as v
Left join
Transactions as T
on v.visit_id =T.visit_id
where T.transaction_id is Null
group by customer_id