-- Lists records of second_table from hbtn_0c_0 database
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
