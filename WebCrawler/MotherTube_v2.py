import pickle as pk
from threading import Thread
import pytube
from pytube import Playlist, YouTube
from queue import Queue

class Worker(Thread):
    def __init__(self, queue, id, dlist):
        Thread.__init__(self)
        self.queue = queue
        self.id = id
        self.dlist = dlist
    
    def run(self):
        while self.queue.qsize() > 0:
            link = self.queue.get()
            print(self.id, "download https://www.youtube.com%s" % link)
            try:
                yt = YouTube("https://www.youtube.com%s" % link)
                yt.streams.filter(only_audio=True, subtype="mp4").first().download("audio/")
                dlist.append(link)
                pk.dump(dlist, open("dlist.pkl", 'wb'))
                print(self.id, "done")
            except Exception as e:
                print(self.id, 'err\n' + str(e))

if __name__ == "__main__":
    mother_playlist = Playlist("https://www.youtube.com/playlist?list=LLG5oSI03yyAlKazKyyePiMQ")

    dlist = list()
    try: dlist = pk.load(open("dlist.pkl", 'rb'))
    except FileNotFoundError: pass

    download_queue = Queue()

    for link in mother_playlist.parse_links():
        if link not in dlist:
            download_queue.put(link)
    
    tlist = list()
    for i in range(16):
        tlist.append(Worker(download_queue, i, dlist))
        tlist[-1].start()

    for t in tlist:
        t.join()

    pk.dump(dlist, open("dlist.pkl", 'wb'))
    print("All done")