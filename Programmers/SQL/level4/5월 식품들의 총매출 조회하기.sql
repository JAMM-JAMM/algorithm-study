-- 코드를 입력하세요
select
    a.PRODUCT_ID
    , a.PRODUCT_NAME
    , SUM(b.AMOUNT) * a.PRICE as TOTAL_SALES
from FOOD_PRODUCT a
    join FOOD_ORDER b on a.PRODUCT_ID = b.PRODUCT_ID
where month(b.PRODUCE_DATE) = 5
group by a.PRODUCT_ID
order by 3 desc, 1 asc
;