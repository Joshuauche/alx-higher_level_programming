-- script that lists all shows contained in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = show_id
LEFT JOIN tv_genres
ON tv_shows.id = show_id
AND tv_genres.id = genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
ASC;
