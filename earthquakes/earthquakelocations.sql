SELECT n_name as country, l_longitude as longitude, l_latitude as latitude
FROM NATION, LOCATION
WHERE l_nationKey = n_nationKey