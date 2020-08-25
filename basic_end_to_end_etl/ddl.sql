create schema stackoverflow_filtered

set search_path to stackoverflow_filtered;

create table results (
	question_id int,
	user_id int,
	answer_id int,
	answer_body text,
	answer_score int,
	answer_comment_count int,
	answer_created_at text,
 	title varchar(300),
 	question_body text,
 	accepted_answer_id int,
 	question_score int,
 	view_count int, 
 	question_comment_count int,
 	question_created_at text,
 	display_name varchar(50),
 	reputation int, 
 	website_url varchar(300),
 	location varchar, 
 	about_me text,
 	views int,
 	up_votes int,
 	down_votes int,
 	image_url varchar(300),
 	user_created_at varchar, 
 	updated_at varchar,
 	City varchar,
 	Country varchar
);



--creating a btree index on reputation
create index reputation_index on results
--creating a hash index on display name
create index display_name on results using hash;


--creating a view 
create view normal_view as 
	select display_name, city, questions_id from results
		where accepted_answer_id is not null;


	
--creating a materialized view
create materialized view materialized_view as 
	select display_name, city, questions_id from results
		where accepted_answer_id is not null;
	
	

