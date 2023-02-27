-- 코드를 입력하세요
select
    a.CATEGORY
    , sum(b.SALES) as sum_sales_per_category
from BOOK a
    join BOOK_SALES b on a.BOOK_ID = b.BOOK_ID
where month(b.SALES_DATE) = 1
group by a.CATEGORY
order by a.CATEGORY
;