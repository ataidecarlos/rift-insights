USE master;
GO
CREATE DATABASE riot_db
ON (
    NAME = riot_db,
    FILENAME = '/mnt/ext_dbs/riot_db.mdf',
    SIZE = 1GB,
    MAXSIZE = 50GB,
    FILEGROWTH = 1GB
    )
LOG ON (
    NAME = riot_db_log,
    FILENAME = '/mnt/ext_dbs/riot_db_log.ldf',
    SIZE = 1GB,
    MAXSIZE = 50GB,
    FILEGROWTH = 1GB
    )
;
GO

-- Enable contained database authentication at the server level
EXEC sp_configure 'contained database authentication', 1;
RECONFIGURE;

-- Enable contained authentication for a specific database
USE [master];
GO
ALTER DATABASE [riot_db] SET CONTAINMENT = PARTIAL;
GO

USE riot_db;
GO

create user [riot_crawler] with password = 'xxxxxxxxxxxxxxxxxxxxxxxx';

grant connect to [riot_crawler];
alter role db_datareader add member [riot_crawler];
alter role db_datawriter add member [riot_crawler];

drop table if exists matches;
create table matches (
    region varchar(10),
    server varchar(10),
    match_id bigint,
    result smallint null,
    constraint pk_matches primary key nonclustered (region, server, match_id)
);

create nonclustered index ix_matches_match_id
on matches (match_id);

-- Known existing match, just to test the connection
--
-- insert into matches (region, server, match_id, result)
-- values ('europe', 'euw1', 7300745146, -200);


CREATE TABLE servers (
    server VARCHAR(10) NOT NULL,
    server_name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL,
    server_h INT IDENTITY PRIMARY KEY
    );
GO

INSERT INTO servers (server, server_name, region)
    VALUES
    ('BR1', 'Brazil', 'AMERICAS'),
    ('NA1', 'North America', 'AMERICAS'),
    ('LA1', 'Latin America North', 'AMERICAS'),
    ('LA2', 'Latin America South', 'AMERICAS'),
    ('EUN1', 'Europe Nordic & East', 'EUROPE'),
    ('EUW1', 'Europe West', 'EUROPE'),
    ('TR1', 'Turkey', 'EUROPE'),
    ('RU', 'Russia', 'EUROPE'),
    ('KR', 'Korea', 'ASIA'),
    ('JP1', 'Japan', 'ASIA'),
    ('PH2', 'Philippines', 'SEA'),
    ('SG2', 'Singapore', 'SEA'),
    ('TH2', 'Thailand', 'SEA'),
    ('TW2', 'Taiwan', 'SEA'),
    ('VN2', 'Vietnam', 'SEA'),
    ('OC1', 'Oceania', 'SEA');
GO