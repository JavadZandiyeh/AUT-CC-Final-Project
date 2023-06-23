from datetime import datetime
from time import sleep

while True:
    print(f"Starting at {datetime.now()}")
    sleep(5)
    print(f"Ending 5 seconds later at {datetime.now()}")