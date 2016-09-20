This program will dynamically create a webpage displaying movie information 
and trailers. entertainment_center.py has the data about the movies and 
is run to create the webpage. It also calls upon media.py for the Movie() 
function to interpret the data, and fresh_tomatoes.py to style and script 
the webpage. fresh_tomatoes.py was provided and small changes were made to 
the styling to improve it.

#Update 9/19/2016
-----------------

	*Updated 2001: A Space Odessey and Inception posters after old image urls expired
	*Started repository to submit to GitHub
	*Changed README.TXT to README.MD and changed formatting

#List of files
--------------

	*entertainment_center.py: stores the data about the movies 
		and is run to generate the page
	*fresh_tomatoes.py: style and scripting for the webpage
	*media.py: defines the Movie() function which handles data about the movies
	*fresh_tomatoes.pyc: compiled version of fresh_tomatoes.py
	*media.pyc: compiled version of media.py
	*fresh_tomatoes.html: the webpage generated from fresh_tomatoes.py
	*README.md: this readme file

#Changes to fresh_tomatoes.py
-----------------------------
	*Line 21: Reduced top padding so everything fits
	*Line 24: Recentered trailer by reducing top margin
	*Lines 25-26: Doubled dimensions of trailer
	*Lines 39-40: Margin and padding reduced so everything fits
	*Line 92: Changed background color to a darker shade
	*Line 128: Changed font color to complement background color
	*Line 129: Displayed storyline data underneath title
	*Line 151: Defined movie_storyline so that code on line 129 works


Best viewed on Google Chrome, 1920x1080 resolution