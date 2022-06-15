import schedule
import time
import os
# import the modules
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

def execute():
    os.system("crimerecognitionmodel.py")
    print("done")


if __name__ == "__main__":
    # Set the format for logging info
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Set format for displaying path
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # Initialize logging event handler
    event_handler = LoggingEventHandler()

    # Initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # Start the observer
    observer.start()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

schedule.every().day.at("00:05").do(execute)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)