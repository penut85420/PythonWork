import pickle as pk

import pytube
from pytube import Playlist, YouTube

mother_playlist = Playlist("https://www.youtube.com/playlist?list=LLG5oSI03yyAlKazKyyePiMQ")

dlist = []

try: dlist = pk.load(open("dlist.pkl", 'rb'))
except FileNotFoundError: pass

dlist.append("/watch?v=vOMQsZ47zTk")
dlist.append("/watch?v=Vdjkzij7pdI")

for link in mother_playlist.parse_links():
    if link not in dlist:
        print("download https://www.youtube.com%s" % link, end='')
        try:
            yt = YouTube("https://www.youtube.com%s" % link)
            yt.streams.filter(only_audio=True, subtype="mp4").first().download("audio\\")
            dlist.append(link)
            pk.dump(dlist, open("dlist.pkl", 'wb'))
            print(" done")
        except pytube.exceptions.RegexMatchError as e:
            print(' err\n' + str(e))
        except AttributeError as e:
            print(' err\n' + str(e))

pk.dump(dlist, open("dlist.pkl", 'wb'))
print("All done")
