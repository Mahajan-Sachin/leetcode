# Write your MySQL query statement below
select T2.unique_id,T1.name from Employees as T1 left join EmployeeUNI as T2 on T1.id=T2.id