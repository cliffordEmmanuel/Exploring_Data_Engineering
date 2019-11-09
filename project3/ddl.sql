create schema stackoverflow_filtered

set search_path to stackoverflow_filtered;

create table results(
	question_id text not null,
	user_id text not null primary key,
	display_name text null,
	reputation text null,
	website_url text null,
	"location" text null,
	about_me text null,
	"views" text null,
	up_votes text null,
	down_votes text null,
	image_url text null,
	user_created_at text null,
	user_updated_at text null,
	city text null,
	country text null,
	title text null,
	question_body text null,
	accepted_answer_id text null,
	question_score text null,
	view_count text null,
	comment_count text null,
	question_created_at text null,
	answer_id text null,
	answer_body text null,
	answer_score text null,
	answer_comment_count text null,
	answer_created_at text null
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
	
	

