import pyinotify
import threading

import logging

class Blacklist(pyinotify.ProcessEvent):

    def __init__(self, filename="blacklist.txt"):
        self.blacklist = []
        self.filename = filename
        self.blacklist = self.read(filename)
        self.lock = threading.Lock()
        wm = pyinotify.WatchManager()
        wm.add_watch('./blacklist.txt', pyinotify.IN_MODIFY, rec=True)
        handler = self
        notifier = pyinotify.ThreadedNotifier(wm, handler)
        notifier.start()
        logging.debug("Blacklist initialized")
        pass

    def read(self, filename="blacklist.txt"):
        logging.debug("Blacklist Data Refresh")
        data = self.blacklist
        try:
            with open(filename, "r") as fp:
                data = fp.read().split("\n")
                data = sorted(data, key=len, reverse = True)
        except Exception as E:
            logging.error("Error: {}\nUsing the old data".format(E))
            data = self.blacklist
        return data
        pass
    
    def process_IN_MODIFY(self, event):
        logging.debug("Blacklist MODIFY event:", event.pathname)
        self.lock.acquire()
        self.blacklist = self.read(self.filename)
        self.lock.release()


    def simplesearch(self, keyword):
        for pattern in self.blacklist:
            logging.debug("pattern: {} entry: {}".format(pattern, keyword))
            flag = keyword.find(pattern)
            if flag != -1:
                return True
        return False

    def search(self, keyword):
        keysplit = keyword.split(".")
        klen = len(keysplit)
        ngram = {}
        result = False
        for l in range(1, klen+1):
            ngram[l] = self.ngrams(keysplit, l)
        for pattern in self.blacklist:
            plen = len(pattern.split("."))
            if plen > klen:
                continue
            if pattern in ngram[plen]:
                result = True
                logging.debug("{} was found in list? : {}".format(keyword, result))
                return result
        result = False
        logging.debug("{} was found in blacklist? : {}".format(keyword, result))
        return result

    def ngrams(self, input, n):
        # input = input.split('.')
        output = []
        for i in range(len(input)-n+1):
            output.append(".".join(input[i:i+n]))
        return output

    def __str__(self):
        return str(self.blacklist)
    pass

if __name__ == "__main__":
    B = Blacklist()
    logging.debug(B)
    logging.debug(B.search("reddit.com"))
    pass