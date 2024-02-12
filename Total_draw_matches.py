import requests

def getTotalDrawMatches():
    response = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year=2011")
    data = response.json()
    total_pages = data['total_pages']
    matches_count = 0
    draw_matches = 0
    for i in range(1,total_pages+1):
        response = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year=2011&page={i}")
        data = response.json()
        matches = data['data']
        for match in matches:
            matches_count+=1
            if match['team1goals']==match['team2goals']:
                draw_matches+=1

    return draw_matches
        
print("total_matches", matches_count)
print(getTotalDrawMatches())
