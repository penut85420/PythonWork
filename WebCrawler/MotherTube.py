import pickle as pk
from threading import Thread
import pytube
from pytube import Playlist, YouTube

mother_playlist = Playlist("https://www.youtube.com/playlist?list=LLG5oSI03yyAlKazKyyePiMQ")

dlist = []

try: dlist = pk.load(open("dlist.pkl", 'rb'))
except FileNotFoundError: pass

# dlist.append("/watch?v=vOMQsZ47zTk")
# dlist.append("/watch?v=Vdjkzij7pdI")

for link in mother_playlist.parse_links():
    if link not in dlist:
        print("download https://www.youtube.com%s" % link, end='')
        try:
            yt = YouTube("https://www.youtube.com%s" % link)
            yt.streams.filter(only_audio=True, subtype="mp4").first().download("audio/")
            dlist.append(link)
            pk.dump(dlist, open("dlist.pkl", 'wb'))
            print(" done")
        except pytube.exceptions.RegexMatchError as e:
            print(' err\n' + str(e))
        except AttributeError as e:
            print(' err\n' + str(e))

pk.dump(dlist, open("dlist.pkl", 'wb'))
print("All done")

# from threading import Thread
# import queue

# class Worker(Thread):
#     def __init__(self, queue, id):
#         Thread.__init__(self)
#         self.queue = queue
#         self.id = id
    
#     def run(self):
#         while self.queue.qsize() > 0:
#             d = self.queue.get()
#             print(self.id, d)

# myq = queue.Queue()

# for i in range(1, 50):
#     myq.put(i)

# t = []
# for i in range(1, 5):
#     t.append(Worker(myq, i))
#     t[-1].start()

# for tt in t:
#     tt.join()

# print("End")