INSERT INTO `create_carrefour_table`.`carrefour_coordinate` (`id`, `position`, `X`, `Y`) 
VALUES ('4', '43_3', '1042', '362');

select * from carrefour_coordinate;
select * from carrefour_4;

update carrefour_4
set 
	X = 1050,
    Y = 320
where 區域 = '43' and 櫃子數 > '3' and 櫃子數 < '7' and 左1右2 = '1';

select * from carrefour_4
where 區域 = '43' and 櫃子數 > '3' and 櫃子數 < '7' and 左1右2 = '1';

select * from carrefour_coordinate;