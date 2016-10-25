# README #

###CS322 Project 4: Brevet Time Calculator###
###Author: Marc Leppold###

##Project Notes

The fourth project of CS322. A calculator for the opening and closing times of brevet controles. Brevets are long distance bicycling events where riders must visit numerous controles along the way, essentially checkpoints, to receive proof of passage. Each controle has an opening and closing time based on the maximum/minimum speed riders can travel for that segment of the race. This program takes the distance of the brevet and the distance of each controle, then finds the opening and closing time for each controle.

The max/min speeds are as follows:
```
dist.         min       max
0-200km       15	    34
200-400km	  15	    32
400-60km0	  15	    30
600-1000km	  11.428	28
1000-1300km	  13.333	26
```
Note: distances are in km, speeds are in km/h

For example, let's say we have a brevet with a total distance of 400km and controles at distances of 140km, 270km and 410km. The maximum speed for the first 200km of a brevet is 34 km/h, so the first control opens after 140/34 hours, or 4 hours and 6 minutes. In the same vein, the minimum speed for a rider is 15 km/h for the first 600km of a brevet, so the same controle closes 9 hours and 20 minutes after the brevet starts.

There are a few quirks to consider when calculating the opening and closing times, though. When we start to calculate the opening and closing time for the controle at 270km, one might think it belongs in the 200-400km category and thus has a max/min speed of 32/15, but this inclination is incorrect. Instead, it belongs to both the 0-200 category and 200-400 category. We calculate its opening and closing times based on the distances it extends into each category - in this case, the first 200km are in the 0-200 range and the last 70km are in the 200-400km range. Thus its opening time is (200/34) + (70/32) hours after start and its closing time is (200/15) + (70/15) hours after start. This program accommodates these quirks in the formula.

One other point of consideration: our sample brevet has a controle at 410km despite the brevet itself being only 400km. Is this invalid? Strangely enough, it's not. Controles are accepted even if they're further than the brevet distance. The restriction on this rule is that they can't be more than 20% further than the brevet. So 410km is a perfectly valid controle distance for our sample brevet, but 500km is not. The furthest possible controle would be at 480km. An important detail is that controles further than the total brevet distance are treated as if they were exactly on that distance. So our 410km controle would have an opening time of (200/34) + (200/32) hours and a closing time of (200/15) + (200/15) hours, as if it was a 400km one. This program accounts for this oddity as well.

Only handles brevets of 200, 300, 400, 600 or 1000 km. Contains some automated nose tests.

Utilizes Flask, Jinja2, MarkupSafe, Werkzeug, arrow, itsdangerous, python-dateutil, six and nose. All of them are supplied with the configure script.


### USAGE ###

Via terminal, enter the directory the program is located in, then execute:
```
configure*   [or . configure, depends on system]
make run
```

Once the program is running, enter
```
HOST:PORT
```
into an internet browser, where HOST matches the IP address of the host computer and PORT matches the port the server is running on (default 5000). Note that there are various dependancies that will likely require executing the configure script first.

Contains automated tests via nose: in the program directory, enter
```
nosetests tests_brevet
```
after configure to perform the tests.
