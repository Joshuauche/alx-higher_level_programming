-- Write a script that updates the score of Bob to 10 in the table second_table
-- allowed to use Bob’s name field
UPDATE `second_table`
SET
`score` = 10
WHERE `second_table`.`name` = 'Bob';
