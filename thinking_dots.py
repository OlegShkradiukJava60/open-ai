import threading
import sys
import time
def start_thinking_dots(label: str, interval: float = 0.5):
    stopEvent = threading.Event()
    def worker():
        sys.stdout.write(label)
        sys.stdout.flush()
        dots = 0
        while not stopEvent.is_set():
            sys.stdout.write(".")
            sys.stdout.flush()
            dots += 1
            if dots % 20 == 0:
               sys.stdout.write("\n"+ label)
               sys.stdout.flush()
            time.sleep(interval) 
    t = threading.Thread(target=worker) 
    t.start()
    return stopEvent           