-- 코드를 입력하세요
with temp_01 as (
    select
        PRODUCT_ID
        , PRODUCT_NAME
        , PRODUCT_CD
        , CATEGORY
        , PRICE
        , max(PRICE) over() as max_price
    from FOOD_PRODUCT
)
select
    PRODUCT_ID
    , PRODUCT_NAME
    , PRODUCT_CD
    , CATEGORY
    , PRICE
from temp_01
where PRICE = max_price;