--  Script that lists the number of records with the same score in the table second_table
--  The list should be sorted by the number of records (descending)

SELECT score COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
