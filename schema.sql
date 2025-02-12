create user [crawler] with password = 'xxxxxxxxxxxxxxxxxxxxxxxx';

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