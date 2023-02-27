-- 코드를 입력하세요
select
    a.ANIMAL_ID
    , a.NAME
from ANIMAL_OUTS a
    left join ANIMAL_INS b on a.ANIMAL_ID = b.ANIMAL_ID
where b.DATETIME is null
order by 1, 2
;