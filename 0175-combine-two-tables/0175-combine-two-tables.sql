# Write your MySQL query statement below
select firstName,lastName,city,state from Person as P Left join address as A on P.personId=A.personId