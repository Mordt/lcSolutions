Consider you are a photographer that takes photos in soccer games.
You are given the task to take a photo of opposing teams in each game.
The photo consists of 2 rows of players and must follow following rues,

1. A player in the back row must be taller than the player in front of him
2. All players in a row must be of the same team

Assuming both teams have the same number of players,
design a function that takes as input two teams (team1, team2) and heights of the players in the teams and
check if it is possible to place the players of team1 in front of team2 in the same photo following the above rules.

Ex:

input:
team1 = [10, 13, 9 , 4]
team2 = [11, 5, 2, 8]  

Answer: False

input:
team1 = [11, 5, 2, 8]
team2 = [10, 13, 9 , 4]

Answer: True

#team 1 is always in front
def isPossible(self, team1, team2):
    #assume both teams exist, with same number of players
    team1.sort()
    team2.sort()
    
    for i, x in enumerate team1:n
        if x >= team2[i]:
            return false
        
    return true
    
    #example
    t1[4, 5, 8, 11] 
    t2[4, 9, 10 , 13]  #return true
    #time comp: 2(nlogn)+n


    
    
Now consider how to generalise the above solution when you have a large number of teams and
you need to find the maximum number of teams (rows) that you can put in a single photo.
Pick a data structure that can represent teams and the relationship between them based on whether they can be in the same photo (following the rules mentioned earlier)
Implement how to find the maximum number of teams that can be in a single photo.

input:
team1 = [11, 5, 2, 8]<
team2 = [6, 10, 14, 14]<taller
team3 = [2, 15, 3, 5]
team4 = [10, 13, 9 , 4]

Answer = 3
(teams 1, 4, 2 can be in the same photo in that order) 

    
#what is the max teams could we photograph while adhering to the above restriction?
#not necessarily in order of input

 [1, 1, 1, 1] 
 [2, 2, 2, 2] 
 
 1 -> 4, 2
 2 -> 
 3 -> 
 4 -> 2
 
 ----
 1 -> 4 -> 2
   -> 2
 3 ->
 
def findTeams(self, teams):
    #have list of teams in order of height
    map 