-- 코드를 입력하세요
select BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    case when STATUS = 'DONE' then '거래완료'
         when STATUS = 'SALE' then '판매중'
         else '예약중'
    end as STATUS
from USED_GOODS_BOARD
where substr(CREATED_DATE, 1, 10) = '2022-10-05'
order by BOARD_ID desc
;