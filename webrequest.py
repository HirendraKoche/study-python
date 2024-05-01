import requests
import setupLog
import logging
from collections import Counter

setupLog.setupLog()
logger = logging.getLogger("study.webRequestStudy")

url = "https://restcountries.com/v3.1/all"

response = requests.get(url)

match response.status_code:
    case 200:
        langs = []
        for item in response.json():
            if "languages" in item:
                langs += item['languages'].values()
        langCounter = Counter(langs)
        logger.info(langCounter.most_common(10))
        logger.info(len(langCounter.keys()))
    case 404:
        print("Page not found")
    case _:
        print("End...")