-- lists record of names and scores(base of order)
--without counting names with no value
select score,name from second_table
where name is not null or name !=""
order by score desc;