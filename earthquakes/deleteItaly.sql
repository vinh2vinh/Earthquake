DELETE 
FROM Nation
WHERE n_nationKey in (SELECT n_nationKey 
                FROM Nation, Location
                WHERE n_nationKey = 2
                AND n_nationKey = l_nationKey
                AND n_name = 'Italy')
;