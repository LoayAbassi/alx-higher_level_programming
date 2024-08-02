-- creates second table and adds new records to them
create table if not exists second_table(
    id int,
    name varchar(256),
    score int
);
insert into second_table(id,name,score) values(1,"John",10);
insert into second_table(id,name,score) values(2,"Alex",3);
insert into second_table(id,name,score) values(3,"Bob",14);
insert into second_table(id,name,score) values(4,"George",8);