import requests

def getTotalGoals(team, year):
    response1 = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}")  
    response2 = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}")
    data1 = response1.json()
    data2 = response2.json()
    total_pages1 = data1['total_pages']
    total_pages2 = data2['total_pages']
    total_pages = total_pages1+total_pages2 
    team1goals_count = 0
    team2goals_count = 0
    for i in range(1,total_pages+1):
        response1 = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={i}")  
        response2 = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={i}")
        data1 = response1.json()
        data2 = response2.json()
        matches1 = data1['data']
        matches2 = data2['data']
        for match in matches1:
            per_match_goal1 = match['team1goals']
            team1goals_count+=int(per_match_goal1)

        for match in matches2:
            per_match_goal2 = match['team2goals']
            team2goals_count+=int(per_match_goal2)
    
    total_goals = team1goals_count+team2goals_count
    return total_goals

print(getTotalGoals('Chelsea', 2014))
