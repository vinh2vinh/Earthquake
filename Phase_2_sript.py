import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")



def Q1(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1: Prints the full Table")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q2(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2: Print all earthquakes in Greece")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey = 3
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" ,Column_header[7],"|",Column_header[8],"|")
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q3(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3: Prints all earthquakes in Italy")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey = 2
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q4(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4: Only prints earthquakes in Japan")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey = 1
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q5(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5: Prints all causes of an earthquake")

    cursor = conn.execute('''SELECT DISTINCT c_natural
    FROM CAUSE
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print("|",Column_header[0],"|")
    for item in queries:
        print(item[0])
            

    print("++++++++++++++++++++++++++++++++++")


def Q6(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6: prints earthquakes based on date(new to old)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY d_date DESC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q7(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7: prints earthquakes based on date(old to new)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY d_date ASC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q8(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8: prints Earthquakes based on depth (hi to low)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY s_depth ASC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q9(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9: prints Earthquakes based on depth (low to hi)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY s_depth DESC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q10(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10: prints the location of earthquakes")

    cursor = conn.execute('''SELECT n_name as country, l_longitude as longitude, l_latitude as latitude
    FROM NATION, LOCATION
    WHERE l_nationKey = n_nationKey
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|")
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|")
            

    print("++++++++++++++++++++++++++++++++++")

def Q11(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11: Prints all earthquakes in 2016")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND d_date <= "2016-12-31"
    AND d_date >= "2016-01-01"
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q12(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12: Prints eastward earthquakes")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY l_latitude ASC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q13(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13: Prints all westward earthquakes")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY l_latitude DESC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q14(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14: Prints all northward earthquakes")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY l_longitude ASC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q15(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15: Prints all southward earthquakes")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    ORDER BY l_longitude DESC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q16(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q16: Prints earthquakes based on magnitude(hi to low)")

    cursor = conn.execute('''
    SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey != 3
    ORDER BY s_magnitude DESC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")

def Q17(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q17: Prints earthquakes based on magnitude(low to hi)")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND n_nationkey != 3
    ORDER BY s_magnitude ASC
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q18(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q18: Prints all nations")

    cursor = conn.execute('''SELECT n_name
    FROM Nation
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0])
    for item in queries:
        print(item[0] )
            

    print("++++++++++++++++++++++++++++++++++")

def Q19(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q19: Prints all earthquakes not in 2016")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND d_date NOT IN (SELECT d_date
                        FROM Date
                        WHERE d_date <= "2016-12-31"
                        AND d_date >= "2016-01-01")
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q20(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q20: Prints only natural earthquakes")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND c_tf = 1
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q21(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q21: Prints only unnatural earthquakes")

    cursor = conn.execute('''SELECT n_name as country,c_natural as nature, l_longitude as longitude, l_latitude as latitude, d_date as date, s_magnitude as magnitude, s_depth as depth, t_timeZone as timezone, t_time as time
    FROM Nation, Location, Cause, Date, Strength, Time
    WHERE l_nationKey = n_nationKey
    AND l_naturalKey = c_naturalKey
    AND d_dateKey = l_dateKey
    AND l_magKey = s_magKey
    AND t_timeKey = l_timeKey
    AND c_tf = 2
    ;''')
    queries = cursor.fetchall()
    Column_header = [i[0] for i in cursor.description]
    print(Column_header[0],"|",Column_header[1],"|",Column_header[2],"|",Column_header[3],"|",Column_header[4],"|",Column_header[5],"|",Column_header[6],"|",Column_header[7],"|",Column_header[8],"|" )
    for item in queries:
        print(item[0] ,"|", item[1],"|",item[2],"|",item[3],"|",item[4],"|",item[5],"|",item[6],"|",item[7],"|",item[8])
            

    print("++++++++++++++++++++++++++++++++++")


def Q22(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q22: deletes Greece from nations")

    cursor = conn.execute('''
    DELETE 
    FROM Nation
    WHERE n_nationKey in (SELECT n_nationKey 
                    FROM Nation, Location
                    WHERE n_nationKey = 3
                    AND n_nationKey = l_nationKey
                    AND n_name = 'Greece')
    ;''')
            

    print("++++++++++++++++++++++++++++++++++")


def Q23(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q23: deletes Italy from nations")

    cursor = conn.execute('''DELETE 
    FROM Nation
    WHERE n_nationKey in (SELECT n_nationKey 
                    FROM Nation, Location
                    WHERE n_nationKey = 2
                    AND n_nationKey = l_nationKey
                    AND n_name = 'Italy')
    ;''')
            

    print("++++++++++++++++++++++++++++++++++")


def Q24(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q24: Deletes Japan from nations")

    cursor = conn.execute('''DELETE 
    FROM Nation
    WHERE n_nationKey in (SELECT n_nationKey 
                    FROM Nation, Location
                    WHERE n_nationKey = 1
                    AND n_nationKey = l_nationKey
                    AND n_name = 'Japan')
    ;''')
            

    print("++++++++++++++++++++++++++++++++++")


def Q25(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q25: Deletes Natural from Cause")

    conn.execute('''DELETE 
    FROM Cause
    WHERE c_natural in (SELECT c_natural
                    FROM Cause, Location
                    WHERE c_tf = 1
                    AND c_naturalKey = l_naturalKey)
    ;''')
    

    print("++++++++++++++++++++++++++++++++++")


def Q26(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q26: delete Unnatural from Cause")

    cursor = conn.execute('''DELETE 
    FROM Cause
    WHERE c_natural in (SELECT c_natural
                    FROM Cause, Location
                    WHERE c_tf = 2
                    AND c_naturalKey = l_naturalKey)
    ;''')
    
            

    print("++++++++++++++++++++++++++++++++++")

def Q27(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q27: inserts USA into Nations")

    cursor = conn.execute('''
    INSERT INTO Nation(n_name, n_nationKey)
    Values('USA', 4)
    ;''')
    
            

    print("++++++++++++++++++++++++++++++++++")

def Q28(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q29: inserts Canada into Nations")

    cursor = conn.execute('''
    INSERT INTO Nation(n_name, n_nationKey)
    Values('Canada', 5)
    ;''')
    
            

    print("++++++++++++++++++++++++++++++++++")





def main():
    database = r"test.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:

        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)
        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)
        Q10(conn)
        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)
        Q15(conn)
        Q16(conn)
        Q17(conn)
        Q18(conn)
        Q19(conn)
        Q20(conn)
        Q21(conn)
        Q22(conn)
        Q23(conn)
        Q24(conn)
        Q25(conn)
        Q26(conn)
        Q27(conn)
        Q28(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()