# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.

# Number of unique matches 

data_ipl = np.genfromtxt(path,delimiter = ",",skip_header = 1,dtype = str)

 # How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.
np.unique(data_ipl[:,0]).size
# Number of unique teams
team1 = np.unique(data_ipl[:,3])
team2 = np.unique(data_ipl[:,4])

#print(team1)
#print(team2)

teams = np.unique(data_ipl[:,3:5])  #all records of 3 and 4 column
print(teams)

#we can use union to join team1 and team2 and perform unique value.
 # this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras
extras = data_ipl[:,17]
extras_int = extras.astype(np.int16)
#print('Extras',sum(extras_int))
print('Extras:',extras_int.sum())


 # An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out

 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.

batsman = 'SR Tendulkar'
play_out_mask = data_ipl[:,20]== batsman

wickets_arr = data_ipl[play_out_mask]

print('when got out:',wickets_arr[:,11])

print('how got out:',wickets_arr[:,21])

#data_ipl[:,11][data_ipl[:,20]==batsman]
# Number of times Mumbai Indians won the toss

toss_winner = 'Mumbai Indians'

toss_winner_mask = data_ipl[:,5] == toss_winner
data_ipl[toss_winner_mask]

Won_toss = np.unique(data_ipl[:,0][toss_winner_mask]).size
print('Mi won toss',Won_toss,'times')
#t2 = data_ipl[toss_team]
#print(len(set(t2[:,0])))


#overall how many matches did MI play?

team_mask = np.logical_or(data_ipl[:,3] == toss_winner, data_ipl[:,4] == toss_winner)
total_matches = np.unique(data_ipl[:,0][team_mask]).size
print('Matches did MI play',total_matches,'toss won',Won_toss)


 # this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixex

 # An exercise to know who is the most aggresive player or maybe the scoring player 
count_six = data_ipl[:,16] == '6'

sixers = data_ipl[count_six]
#print(sixers)
#batsman_six = sixers[:,13]
#print(sixers[:,13])

batsman,counts = np.unique(sixers[:,13],return_counts = True)
#print(batsman)
#print(counts)

#------------------------------------------------
from collections import Counter
most_sixes = Counter(sixers[:,13])
print(most_sixes.most_common(2))






