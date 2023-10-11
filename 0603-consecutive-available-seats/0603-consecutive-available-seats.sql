# Write your MySQL query statement below
SELECT DISTINCT A.seat_id
FROM cinema A JOIN cinema B
ON A.free = 1 AND B.free = 1
AND abs(A.seat_id - B.seat_id) = 1
ORDER BY A.seat_id;
