-- 코드를 입력하세요
select
    b.INGREDIENT_TYPE as INGREDIENT_TYPE
    , SUM(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF a
    join ICECREAM_INFO b on a.FLAVOR = B.FLAVOR
group by INGREDIENT_TYPE
order by 2
;