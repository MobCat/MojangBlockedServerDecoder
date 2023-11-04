#!/env/Python3.10.4
#/MobCat (2023)

import requests
import time
import hashlib
import socket


def checkPing(server: str):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, 25565))
    except OSError as error:
        return False
    else:
        s.close()
        return True

print("Downloading blockedservers list")
response = requests.get('https://sessionserver.mojang.com/blockedservers')

cnt = 0
upcnt = 0
if response.status_code == 200:
	hashList = response.text.splitlines()

	print("Loading and rebuilding dict with wildcards")

	dictRebuild = []
	with open('dict.txt', 'r') as file:
		for line in file:
			url = line.strip()
			#dictRebuild.append(url)

			# Split and concat play.gotpvp.com to
			# gotpvp.com
			# *.gotpvp.com
			# play.gotpvp.com
			# *.play.gotpvp.com
			parts = url.split(".")
			for i in range(len(parts)-2, -1, -1):
				newURL = ".".join(parts[i:])
				dictRebuild.extend([newURL, f"*.{newURL}"])

	# remove and dupes
	dictRebuild = list(set(dictRebuild))  



	with open('decoded.txt', 'w') as output_file:
		for url in dictRebuild:
			sha1 = hashlib.sha1(url.encode()).hexdigest()
			if sha1 in hashList:
				# Ping check to slow, and dosent work corectly.
				'''
				if checkPing(url):
					print(f"1:{sha1}:{url}")
					upcnt += 1
				else:
					print(f"0:{sha1}:{url}")
				cnt += 1
				'''
				print(f"{sha1}:{url}")
				output_file.write(f"{sha1}:{url}\n")
				cnt += 1

			# Wildcard fix, lol no idea whats going on here.
			url2 = f"*.{url}"
			sha1 = hashlib.sha1(url2.encode()).hexdigest()
			if sha1 in hashList:
				print(f"{sha1}:*.{url}")
				output_file.write(f"{sha1}:{url}\n")
				cnt += 1
			
	#print(f"Decoded {cnt}/{len(hashList)}\n{upcnt} Active servers found")
	print(f"Decoded {cnt}/{len(hashList)}")
