-- 코드를 입력하세요
# with temp_01 as (
#     select
#         a.*
#         , b.DATETIME as OUT_DATETIME
#     from ANIMAL_INS a
#         left join ANIMAL_OUTS b on a.ANIMAL_ID = b.ANIMAL_ID
#     order by a.DATETIME
# ), temp_02 as (
#     select
#         *
#         , row_number() over(order by DATETIME) as row_num
#     from temp_01
#     where OUT_DATETIME is null
# )
# select
#     NAME
#     , DATETIME
# from temp_02
# where row_num <= 3
# ;

with temp_01 as (
    select
        a.*
        , b.DATETIME as OUT_DATETIME
        , row_number() over(order by a.DATETIME) as row_num
    from ANIMAL_INS a
        left join ANIMAL_OUTS b on a.ANIMAL_ID = b.ANIMAL_ID
    order by a.DATETIME
)
select
    NAME
    , DATETIME
from temp_01
where OUT_DATETIME is null
and row_num <= 3
;