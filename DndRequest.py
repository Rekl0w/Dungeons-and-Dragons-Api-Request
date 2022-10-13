import requests
response = requests.get("https://www.dnd5eapi.co/api/ability-scores/cha")
print(response.json())

response2 = requests.get("https://www.dnd5eapi.co/api/spells/sacred-flame")
print(response2.json())