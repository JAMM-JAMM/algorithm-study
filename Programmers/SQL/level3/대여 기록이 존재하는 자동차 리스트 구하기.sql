-- 코드를 입력하세요
select
    distinct(a.CAR_ID)
from CAR_RENTAL_COMPANY_CAR a
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY b on a.CAR_ID = b.CAR_ID
where a.CAR_TYPE = "세단"
and b.START_DATE >= '2022-10-01' and b.START_DATE < '2022-11-01'
order by CAR_ID desc
;