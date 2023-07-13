import asyncio
from app import app
from database import persist_todb
import schedule
import time
import ischedule

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def good_luck():
     print("Good Luck for Test")
     asyncio.run(main())



async def main():
    print("hello")
    await persist_todb()
    print("Data generated successfully!")



ischedule.schedule(good_luck, interval=1*60*60)
ischedule.run_loop()
   
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)




