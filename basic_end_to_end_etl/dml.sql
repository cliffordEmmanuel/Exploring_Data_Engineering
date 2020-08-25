--how many cities appeared more than twice?

select count(city) from results 
	having count(city) > 2;
	
--how many unique created_at dates are in the resultant table?

select count(distinct user_created_at) from results 


--awarding the user with the highest reputation
select user_id, display_name from results
	where reputation = ( select max(reputation) from results);