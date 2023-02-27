-- 코드를 입력하세요
select
    PRODUCT_CODE
    , SUM(a.PRICE * b.SALES_AMOUNT) as SALES
from PRODUCT a
    join OFFLINE_SALE b on a.PRODUCT_ID = b.PRODUCT_ID
group by a.PRODUCT_CODE
order by SALES DESC, PRODUCT_CODE ASC
;