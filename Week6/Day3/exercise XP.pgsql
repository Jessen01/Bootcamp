-- 1.Get a list of all film languages.

SELECT DISTINCT * FROM language;


--2. Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
    -- 1.Get all films, even if they don’t have languages.
    -- 2. Get all languages, even if there are no films in those languages.

SELECT film.film_title,film.description,language.name
FROM film
INNER JOIN language ON language.name ; 



-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (
    id SERIAL primary key,
    name VARCHAR(200) NOT NULL
);

INSERT INTO new_film (id,name)
VALUES (1,batman),
       (2,superman),
       (3,catwoman);


-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.
-- It should have the following columns:
    -- review_id – a primary key, non null, auto-increment.
    -- film_id – references the new_film table. The film that is being reviewed.
    -- language_id – references the language table. What language the review is in.
    -- title – the title of the review.
    -- score – the rating of the review (1-10).
    -- review_text – the text of the review. No limit on the length.
    -- last_update – when the review was last updated.

CREATE TABLE customer_review(
    review_id SERIAL NOT NULL,
    film_id SERIAL NOT NULL ,
    language_id SERIAL NOT NULL,
    title_review int,
    score_review int(10),
    reviews VARCHAR,
    last_update date
);

-- 5.Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
    INSERT INTO customer_review(film_id,reviews)
    VALUES('the film is good')
