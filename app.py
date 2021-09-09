import asyncio
import os
import json
import aiohttp
import hashlib
import requests
from shutil import rmtree
import time

start_time = time.time()


async def main():
    req = requests.get("https://api.cdnjs.com/libraries")
    res = json.loads(req.content)["results"]
    urls = [res[_]["latest"] for _ in range(len(res))]

    async with aiohttp.ClientSession() as session:
        for index, url in enumerate(urls):
            try:
                start_time_loop = time.time()
                hash_file = hashlib.md5(url.encode())
                file = hash_file.hexdigest()
                link = url.replace("\n", "")
                if(os.path.exists(file)):
                    rmtree(file)
                else:
                    os.mkdir(file)
                    async with session.get(link) as res:
                        resp = await res.text()
                        with open("{0}/{1}".format(file, f"{file}.txt"), "wb") as f:
                            f.write(resp.encode())
                print(
                    f"{index} ---  {file[::-6]} --- {(time.time() - start_time_loop)} seconds ---")
            except:
                pass

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

# Enter which files you want to download
# with open("urls.txt", "r") as f:
#     urls = f.readlines()

# for e in urls:
#     hash_file = hashlib.md5(e.encode())
#     file = hash_file.hexdigest()
#     url = e.replace("\n", "")
#     if(os.path.exists(file)):
#         rmtree(file)
#     else:
#         os.mkdir(file)
#         rq = requests.get(url)
#         with open("{0}/{1}".format(file, f"{file}.txt"), "wb") as f:
#             f.write(rq.content)
