import requests
import json

_video_id = 360257927
_client_id = "2bkk0r1860f7a9j3mo2leulxkm1dyr"

url_begin = "https://api.twitch.tv/v5/videos/%s/comments?client_id=%s"
url_next = "https://api.twitch.tv/v5/videos/%s/comments?client_id=%s&cursor=%s"

r = requests.get(url_begin % (_video_id, _client_id))

with open('a.json', 'w', encoding='utf8') as fout:
    fout.write(r.text)

msglog = open('msg.log', 'w', encoding='utf8')

j = json.load(open('a.json', 'r', encoding='utf8'))
for m in j['comments']:
    msglog.write(str(m['content_offset_seconds']) + '\t' + m['message']['body'] + '\n')

while j['_next'] != None:
    print(j['_next'], end='\r')
    r = requests.get(url_next % (_video_id, _client_id, j['_next']))
    with open('a.json', 'w', encoding='utf8') as fout:
        fout.write(r.text)
    j = json.load(open('a.json', 'r', encoding='utf8'))
    for m in j['comments']:
        msglog.write(str(m['content_offset_seconds']) + '\t' + m['message']['body'] + '\n')

msglog.close()