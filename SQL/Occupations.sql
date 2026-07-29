SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;
SELECT 
MAX(CASE WHEN OCCUPATION = 'Doctor' THEN NAME END) AS Doctor,
MAX(CASE WHEN OCCUPATION = 'Professor' then name end) as Professor,
max(case when occupation = 'Singer' then name end) as Singer,
max(case when occupation = 'Actor' then name end) as actor
from (
    select name, occupation, row_number() over (partition by occupation order by name) as rn from occupations
)
group by rn
order by rn;
exit;
