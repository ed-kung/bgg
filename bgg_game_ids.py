from xml.dom import minidom
import requests
import time

filename = 'bgg_game_ids.txt'
f = open(filename, 'w')

for i in range(1, 10):
	time.sleep(2)
	url = "https://boardgamegeek.com/sitemap_geekitems_boardgame_page_%d.xml" % i
	r = requests.get(url)
	if r.status_code==200:
		doc = minidom.parseString(r.content)
		locs = doc.getElementsByTagName("loc")
		for loc in locs:
			game_url = loc.firstChild.data
			f.write(game_url.split("/")[4] + '\n')
		print("Got %d" % i)
	else:
		print("Didn't get %d" % i)
	
f.close()

	
	




