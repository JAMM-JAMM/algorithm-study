-- 코드를 입력하세요
with temp_01 as (
    select
        *
        , DATEDIFF(END_DATE, START_DATE) + 1 as DATE_DIFF
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)
, temp_02 as (
    select
        CAR_ID
        , round(avg(DATE_DIFF), 1) as avg_date_diff
    from temp_01
    group by CAR_ID
)
select
    *
from temp_02
where avg_date_diff >= 7
order by avg_date_diff desc, car_id desc
;