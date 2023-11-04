# Mojang Blocked Server Decoder
A quick and dirty python tool for downloading the current blocked server list and checking it with a known list of URLs.

# What is a blocked server?
TL:DR a server that mojang brand enforcement deems to brake the minecraft EULA will end up on this list.<br>
If your server URL is on this list, then a vanilla client will not be able to connect to the server.<br>
If you want to learn more about this, watch TheMisterEpic's video on this subject, video linked by image below.<br>
[![Video Link](https://img.youtube.com/vi/Ag0OZEgk4vg/0.jpg)](https://www.youtube.com/watch?v=Ag0OZEgk4vg)

# How it works
This script will go and download the current blocked server list from<br>
https://sessionserver.mojang.com/blockedservers <br>
Then opens the `dict.txt` dictionary file of known blocked URLs<br>
Then it will rebuild this list to include wildcards<br>
`play.sample.com`<br>
would become
```
sample.com
*.sample.com
play.sample.com
*.play.sample.com
```
Then we SHA1 hash the URLs and check if they are on the banned list.<br>
If they are, they will be saved to a new `decoded.txt` file.<br>

# How to run
First make sure you have the `requests` python library installed.<br>
You can do this by running `pip install requests`<br>
(If you are encountering issues in the future, this script was built with `pip install requests==2.28.0`)<br>
Once that is done, you can simply download the `decoder.py` and `dict.txt` from this repo<br>
place them in the same folder, and then just run `python decoder.py`<br>
Found hashes will be printed to the console, followed by how many hashes it found. <br>
At the time of posting this script, we can decode 146 hashes out of 2316 found on the mojan website.<br>
`Decoded 146/2316`<br><br>

To add to the hash dictionary, you can open the `dict.txt` and place a new url without wildcards on a new line.

# TODO:
There is some dead code in this project for pinging servers to see if they are still active / alive.<br>
However the code takes way to long to run, and pinging a minecraft server is different then pinging a web server so the results were not reliable.<br><br>

Clean up the rebuild URL list to add wildcards code<br>
I'm not 100% sure its even working correctly and in its current form, it's a little bodged<br><br>

Test if we can just "bypass" this blocked server list, by connecting to the servers IP or DNS address, not it's blocked URL.<br><br>

This project was an aside to a larger minecraft server checker project.<br>
This code should and could check more info about minecraft servers, but that's what the other project is for.<br>
