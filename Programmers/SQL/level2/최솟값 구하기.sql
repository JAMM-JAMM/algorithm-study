-- 코드를 입력하세요
with temp_01 as (
    select
        NAME
        , DATETIME
        , row_number() over(order by DATETIME) as row_num
    from ANIMAL_INS
)
select
    DATETIME
from temp_01
where row_num = 1;