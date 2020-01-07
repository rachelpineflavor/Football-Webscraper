from bs4 import BeautifulSoup
import requests

from twilio.rest import Client

url = 'https://www.cbssports.com/nfl/teams/ATL/atlanta-falcons/schedule/regular/'
response = requests.get(url)
content = BeautifulSoup(response.content, 'html.parser')
opposing_team = []
game_date = []
start_time = []
game_location = []
game_channel = []

tables = content.findAll('tbody')
desiredTable = tables[1].findAll('td')

#Finding the opposing team
for row in desiredTable:
    opposing_team.append(row.text.strip()) 
print(opposing_team[2])

#Finding the date of the game
for row in desiredTable:
    game_date.append(row.text.strip()) 
print(game_date[1])

#Finding the start time of the game
for row in desiredTable:
    start_time.append(row.text.strip()) 
print(start_time[3])

#Finding the channel the game is on
for row in desiredTable:
    game_channel.append(row.text.strip()) 
print(game_channel[4])

#Finding the location of the game
for row in desiredTable:
    game_location.append(row.text.strip())
if game_location[5] == 'Mercedes-Benz Stadium':
    print('at home')
else:
    print('away')

#Twilio message
allTogether = 'The next Falcons game is ' + opposing_team[2] + ', ' + game_location[5] + ' ' + 'on ' + \
        game_date[1] + ' ' + 'at ' + start_time[3] + '. ' + 'Watch the game on ' + game_channel[4] + '.'
print(allTogether)

accountSID = 'AC82d079d1a2e13ad4def8b61dde8c6ed6'
authToken = '665bad11a07c96bd50b644e45205895c'
client = Client(accountSID, authToken)
myTwilioNumber = '+16466817321'
destCellPhone = '+15127409869'
myMessage = client.messages.create(body = allTogether, from_=myTwilioNumber, to=destCellPhone)
