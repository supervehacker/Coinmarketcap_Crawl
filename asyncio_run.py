import asyncio
from concurrent.futures import ThreadPoolExecutor
# from selenium import webdriver

from data_master import *

l_tokens = refresh_l_tokens()


async def crawl(token_name):
    from data_worker import DataWorker
    data_worker = DataWorker(token_name)
    data_worker.crawl_single_token()


async def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        # loop = asyncio.get_event_loop()
        # tasks = [loop.run_in_executor(executor, loop.create_task, crawl(token)) for token in l_tokens]
        # tasks = [loop.run_in_executor(executor, loop.create_task, crawl(token)) for token in l_tokens]
        # await asyncio.gather(*tasks)
        tasks = [crawl(token) for token in l_tokens]
        for f in asyncio.as_completed(tasks):
            await f

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
