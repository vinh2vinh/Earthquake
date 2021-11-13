SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
FROM Nation, Location, Cause, Date, Strength, Time
WHERE l_nationKey = n_nationKey
AND l_naturalKey = c_naturalKey
AND d_dateKey = l_dateKey
AND l_magKey = s_magKey
AND t_timeKey = l_timeKey
ORDER BY d_date ASC
;