import csv
import time
from boardgamegeek import BoardGameGeek

bgg = BoardGameGeek()

# first import the game id list
f = open("bgg_game_ids.txt")
idlist = []
for line in f:
	idlist.append(int(line.split()[0]))
f.close()

# data file
datafile = "bgg_games.csv"

# max and min game id 
# (if you don't want to scrape the whole dataset in one go)
min_game_id = 1
max_game_id = 100

# header line (variable names)
header = (	'snapshot_date', \
			'id', \
			'name', \
			'year', \
			'artists', \
			'categories', \
			'designers', \
			'expansion', \
			'expands', \
			'expansions', \
			'families', \
			'implementations', \
			'max_players', \
			'mechanics', \
			'min_age', \
			'min_players', \
			'playing_time', \
			'publishers', \
			'ranks', \
			'rating_average', \
			'rating_average_weight', \
			'rating_bayes_average', \
			'rating_median', \
			'rating_num_weights', \
			'rating_stddev', \
			'users_commented', \
			'users_owned', \
			'users_rated', \
			'users_trading', \
			'users_wanting', \
			'users_wishing')

# comment this part out if data file exists and you are appending
f = open(datafile, 'w', newline='')
csv.writer(f).writerow(header)
f.close()

# begin data collection
f = open(datafile, 'a', newline='')
writer = csv.writer(f)

for id in idlist:
	if (id>=min_game_id and id<=max_game_id):
		print(id, end="")
		print('... ', end="")
		try:
			g = bgg.game(game_id = id)
			line = ( time.strftime("%Y-%m-%d"), \
					g.id, \
					g.name, \
					g.year, \
					(' | '.join(g.artists)), \
					(' | '.join(g.categories)), \
					(' | '.join(g.designers)), \
					g.expansion, \
					str(g.expands), \
					str(g.expansions), \
					(' | '.join(g.families)), \
					(' | '.join(g.implementations)), \
					g.max_players, \
					(' | '.join(g.mechanics)), \
					g.min_age, \
					g.min_players, \
					g.playing_time, \
					(' | '.join(g.publishers)), \
					str(g.ranks), \
					g.rating_average, \
					g.rating_average_weight, \
					g.rating_bayes_average, \
					g.rating_median, \
					g.rating_num_weights, \
					g.rating_stddev, \
					g.users_commented, \
					g.users_owned, \
					g.users_rated, \
					g.users_trading, \
					g.users_wanting, \
					g.users_wishing)
			writer.writerow(line)
		except:
			print('failed... ', end="")

f.close()

			

