-- lists all records <= 10 based on score desc order
select score,name
from second_table
where score >= 10
order by score desc;