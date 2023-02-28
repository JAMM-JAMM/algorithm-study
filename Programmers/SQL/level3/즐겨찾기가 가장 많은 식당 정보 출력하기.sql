-- 코드를 입력하세요
with temp_01 as (
    select
        *
        , row_number() over(partition by FOOD_TYPE order by FAVORITES desc) row_num
    from REST_INFO
)
select
    FOOD_TYPE
    , REST_ID
    , REST_NAME
    , FAVORITES
from temp_01
where row_num = 1
order by FOOD_TYPE desc
;