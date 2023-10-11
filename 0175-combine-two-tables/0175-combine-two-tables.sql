/* Write your T-SQL query statement below */
SELECT A.lastName, A.firstName, B.city, B.state
FROM Person A
LEFT JOIN Address B
ON A.personId = B.personId;

