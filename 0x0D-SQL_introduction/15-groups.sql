-- shows groups having same score
select score, count(score) as "number"
from second_table
group by score;