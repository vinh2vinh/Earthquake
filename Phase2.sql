
CREATE TABLE Cause (
    c_natural varchar(30) NOT NULL,
    c_tf integer NOT NULL,
    c_naturalKey integer NOT NULL 
    
);

CREATE TABLE Nation(
    n_name varchar(30) NOT NULL,
    n_nationKey integer NOT NULL 
);

CREATE TABLE Date(
    d_date varchar(15) NOT NULL,
    d_dateKey integer NOT NULL ,
    d_nationKey integer NOT NULL
);

CREATE TABLE Time(
    t_timeZone varchar(15) NOT NULL,
    t_time varchar(15) NOT NULL,
    t_timeKey integer NOT NULL 
);

CREATE TABLE Strength(
    s_magnitude  decimal(4, 2) NOT NULL,
    s_depth decimal(4, 2),
    s_magKey integer NOT NULL 
);

CREATE TABLE Location(
    l_longitude decimal(7, 4) NOT NULL,
    l_latitude decimal(7, 4) NOT NULL,
    l_dateKey integer NOT NULL,
    l_magKey integer NOT NULL,
    l_timeKey integer NOT NULL,
    l_nationKey integer NOT NULL,
    l_naturalKey integer NOT NULL
);




