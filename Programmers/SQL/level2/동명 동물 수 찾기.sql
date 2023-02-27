-- 코드를 입력하세요
select
    NAME
    , count(*) as cnt
from ANIMAL_INS
group by NAME
having cnt > 1 and NAME is not null
order by name
;