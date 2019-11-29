import json
import os
import requests

#Temporary - permanently set songlink url;
#songlinkurl = 'https://song.link/us/i/466988833'

def getSong(songlinkurl):
    #From song.link
    request = (requests.get('https://api.song.link/v1-alpha.1/links?url=%s'  % (str(songlinkurl)) ).content)

    links = json.loads(request)
    youtube = links.get('linksByPlatform').get('youtube')
    spotify = links.get('linksByPlatform').get('spotify')
    suid = links.get('entitiesByUniqueId').get(spotify.get('entityUniqueId'))
    yuid = links.get('entitiesByUniqueId').get(youtube.get('entityUniqueId'))
    ytid = str(yuid.get('id'))
    url = str(youtube.get('url'))

    artist = str(suid.get('artistName')) #Pulls artist name
    title = str(suid.get('title')) #Pulls song name

    print (("Retreiving %s by %s.") %(title, artist))

    os.system(('youtube-dl --quiet https://www.youtube.com/watch?v={} -x --audio-format mp3 --output \"{} - {}.%(ext)s"').format(ytid, artist, title))

with open ("songs.json") as s:
    s = json.load(s)
    for i in (s):
        try:
            getSong(i)
        except: 
            print (("Song {} unavailable. Retry manually.").format(i))