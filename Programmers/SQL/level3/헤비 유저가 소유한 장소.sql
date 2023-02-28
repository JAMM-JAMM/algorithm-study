-- 코드를 입력하세요
with temp_01 as (
    select
        *
        , count(*) over(partition by HOST_ID) as cnt_host_id
    from PLACES
)
select
    ID
    , NAME
    , HOST_ID
from temp_01
where cnt_host_id >= 2
order by ID
;