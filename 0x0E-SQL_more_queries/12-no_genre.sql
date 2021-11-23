-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
RIGHT JOIN tv_show_genres
ON tv_shows.id = show_id
RIGHT JOIN tv_genres
ON tv_shows.id = show_id
AND tv_genres.id = genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
ASC;
