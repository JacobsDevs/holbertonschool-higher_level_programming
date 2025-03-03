-- Get the score and count of score from second_table 
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score;
ORDER BY score desc;
