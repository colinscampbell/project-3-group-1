create table clean_weather_data as
select w.state State_Code, s.state State ,year, 
round(sum(Jan)/count(distinct county)) Jan_Avg,
round(sum(Feb)/count(distinct county)) Feb_Avg,
round(sum(Mar)/count(distinct county)) Mar_Avg,
round(sum(Apr)/count(distinct county)) Apr_Avg,
round(sum(May)/count(distinct county)) May_Avg,
round(sum(Jun)/count(distinct county)) Jun_Avg,
round(sum(Jul)/count(distinct county)) Jul_Avg,
round(sum(Aug)/count(distinct county)) Aug_Avg,
round(sum(Sep)/count(distinct county)) Sep_Avg,
round(sum(Oct)/count(distinct county)) Oct_Avg,
round(sum(Nov)/count(distinct county)) Nov_Avg,
round(sum(Dec)/count(distinct county)) Dec_Avg
from Weather_Raw w,State_Code s
where w.State = s.Code
group by w.state,Year
