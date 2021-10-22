# GearScore Web API

GearScore is an addon for the game World of Warcraft that calculates a player's item score. It helps in estimating a 
character's readiness for certain dungeons and raid encounters. There is a limited (or close to none) resource on how 
one can check an item's gear score without opening up the game. This web API fills in that gap.

![Screenshot](https://i.imgur.com/4dtt0F1.png)

This project has two parts:
1. A web UI that you can use to view GearScore
2. A web API that is exposed that can be used in other applications (Discord bots, etc.)

## Web UI

When searching an item through wotlkdb.com, replace the **db** part with **gs**. Example: 
* https://wotlkdb.com/?item=54590 to
* https://wotlkgs.com/?item=54590  

![](https://i.imgur.com/hAYf2S3.png)

There might be some variations from the in-game one (depending on which server you are playing, this was designed with
Warmane in mind) but is good enough at least for approximation.

## Web API

The web API can be accessed using a GET method at [https://wotlkgs.com/gs/api/v1/54590](https://wotlkgs.com/gs/api/v1/54590). 
Just replace the last part (54590) with your item id.
![API](https://i.imgur.com/FAsOxja.png)

A Swagger UI can also be accessed through [here](http://wotlkgs.com:8080/swagger/).

# Road Map

Other than the "Random item" that I am currently working on, I consider this project complete. If you have any suggestions
to make it better, feel free to contact me.

# Thanks

* [Snuske](https://github.com/mortenmoulder/Snuske) - got the database of items with GearScore here.
* [Wotlkdb](https://wotlkdb.com/) - not really affiliated with this site, but this is where you search.
* [github1s](https://github1s.com/) - got the inspiration for the implementation here.
