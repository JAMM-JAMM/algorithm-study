with temp_01 as (
    select
        a.ANIMAL_ID
        , a.ANIMAL_TYPE
        , a.NAME
        , a.DATETIME as IN_DATETIME
        , b.DATETIME as OUT_DATETIME
        , DATEDIFF(b.DATETIME, a.DATETIME) as date_diff
    from ANIMAL_INS a
        join ANIMAL_OUTS b on a.ANIMAL_ID = b.ANIMAL_ID
    order by date_diff desc
), temp_02 as (
select
    *
    , row_number() over(order by date_diff desc) as row_num
from temp_01
)
select
    ANIMAL_ID
    , NAME
from temp_02
where row_num <= 2
;