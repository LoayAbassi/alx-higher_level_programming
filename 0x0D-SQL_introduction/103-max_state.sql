-- shows maximum tempreture in each state
select state, max(value) as max_temp
from temperatures 
group by state
order by state;