-- script that displays the max temperature of each state (ordered by State name).

SELECT state,
MAX(column_name)
AS max_temp FROM temperatures
GROUP BY state
ORDER BY max_temp
DESC LIMIT 3;
