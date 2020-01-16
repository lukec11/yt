import json
import os
import requests
import time


count = 0

def getSong(songlinkurl):
    #From song.link
    request = (requests.get('https://api.song.link/v1-alpha.1/links?url=%s'.format(str(songlinkurl)) ).content)

    links = json.loads(request)

    youtube = links['linksByPlatform']['youtube']
    spotify = links['linksByPlatform']['spotify']
    suid = links['entitiesByUniqueId')[spotify['entityUniqueId']
    yuid = links.get('entitiesByUniqueId')[(youtube['entityUniqueId']]
    ytid = str(yuid['id'])
    url = str(youtube['url'])

    artist = str(suid['artistName']) #Pulls artist name
    title = str(suid['title']) #Pulls song name

    print(f"Retreiving {title} by {artist}.")

    os.system((f'youtube-dl --quiet https://www.youtube.com/watch?v={ytid} -x --audio-format mp3 --output \"output/{artist} - {title}.%(ext)s"')

with open ("songs.json") as f:
    s = json.load(f)
for i in s: #this is a crude counter that works to combat Odesli API limits.
    if count >= 10:
        print("Sleeping.")
        time.sleep(60)
        count = 0
    count += 1
    
    try:
        getSong(i)
    except: 
        print ((f"Song {i} unavailable. Retry manually.")
