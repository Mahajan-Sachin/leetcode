# Write your MySQL query statement below
select T1.name as "Customers" from `Customers` as T1 Left join `Orders` as T2 on T1.id=T2.customerId where T2.id is NULL