import fresh_tomatoes
import media


undercover_brother = media.Movie("Undercover Brother", 120, "When "The Man" tries to derail a black candidate's presidential campaign, Undercover Brother and his fellow secret agents come to the rescue.", "http://d3ny4pswk2x1ig.cloudfront.net/dcf82f50c0cb6b1cd6d97c08395b92d6a17f0c151bf5b5ee2ebe5ac1.jpg", "https://www.youtube.com/watch?v=ubV3t9_CwDc", 77, "action comedy" )

this_is_the_end = media.Movie("This is the End", 120, "Nothing ruins a party like the end of the world in this apocalyptic comedy.","http://www.apnatimepass.com/this-is-the-end-movie-wallpaper-3.jpg","https://www.youtube.com/watch?v=Yma-g4gTwlE", "83", "action fantasy"  )

mystery_men = media.Movie("Mystery Men", 120, "They are not your average superheroes.", "http://images.moviepostershop.com/mystery-men-movie-poster-1999-1020211306.jpg", "https://www.youtube.com/watch?v=PKmHBFgIoX0", "60", "Fantasy Indie")

movies = [undercover_brother,  this_is_the_end, mystery_men]
fresh_tomatoes.open_movies_page(movies)

#fresh_tomatoes.open_movies_page(movies)


