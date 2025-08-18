# Write your MySQL query statement below
select T1.id from Weather as T1,Weather as T2
where
datediff(T1.recordDate,T2.recordDate)=1 and 
T1.temperature>T2.temperature