with A01 as (
    select BOARD_ID
    from (
        SELECT BOARD_ID
            , row_number() over(order by VIEWS desc) as RID
        from USED_GOODS_BOARD
    ) A
    where RID = 1
)
-- 
-- concat('/home/grep/src/',A.BOARD_ID,'/',B.FILE_ID,B.FILE_NAME,B.FILE_EXT) as FILE_PATH
select '/home/grep/src/'||A.BOARD_ID||'/'||B.FILE_ID||B.FILE_NAME||B.FILE_EXT as FILE_PATH
from A01 A
    , USED_GOODS_FILE B
where A.BOARD_ID = B.BOARD_ID
order by B.FILE_ID desc
;