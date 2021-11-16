DELETE 
FROM Cause
WHERE c_natural in (SELECT c_natural
                FROM Cause, Location
                WHERE c_tf = 1
                AND c_naturalKey = l_naturalKey
                AND n_natural = 'nature')
;