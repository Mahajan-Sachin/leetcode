# Write your MySQL query statement below
select distinct T1.num as  ConsecutiveNums
from Logs as T1
join Logs as T2 on T1.id=T2.id-1
join Logs as T3 on T1.id=T3.id-2
where T1.num=T2.num and T2.num =T3.num;