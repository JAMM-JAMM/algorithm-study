-- 코드를 입력하세요
with temp_01 as (
    select
        *
    from APPOINTMENT
    where month(APNT_YMD) = 5
)
select
    MCDP_CD as 진료과코드
    , count(*) as 5월예약건수
from temp_01
group by MCDP_CD
order by 2, 1
;