import os
import re
import requests
from shutil import rmtree

with open("urls.txt", "r") as f:
    urls = f.readlines()

for e in urls:
    url = e.replace("\n", "")
    directory = re.search(r'https://www.(.*?).com', e).group(1)
    file_name = "{0}.txt".format(directory)
    if(os.path.exists(directory)):
        rmtree(directory)
    else:
        os.mkdir(directory)
        rq = requests.get(url)
        with open("{0}/{1}".format(directory, file_name), "wb") as f:
            f.write(rq.content)
