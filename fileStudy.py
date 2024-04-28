# Learning file handling

import logging
from setupLog import setupLog
import json
from collections import Counter
import re

setupLog()
logger = logging.getLogger("study.fileStudy")

# Write a function which count number of lines and number of words in a text.
def countLineWords(file):
    logger.info("Start countLineWords function")
    linecount = 0
    wordcount = 0
    try:
        logger.debug(f"Openning {file} for reading")
        with open(file, 'rt', encoding='utf-8') as f:
            logger.debug("Reading single line.")
            line = f.readline().strip()
            logger.debug(f"First Line --> {line}")
            while line != "":
                linecount += 1
                wordcount += len(line.split())
                line = f.readline().strip()
                logger.debug(f"Next line --> {line}")
    except Exception as e:
        logger.exception(e)
    else:
        logger.info(f"Result.\nLines = {linecount}\nWords = {wordcount}")
        return linecount, wordcount
    finally:
        logger.info("End countLineWords function")

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def mostSpokenLang(fname, outputno):
    logger.info("Start mostSpokenLang function")
    langCount = {}
    try:
        logger.debug(f"Reading file {fname}")
        with open(fname, 'rt', encoding='utf-8') as f:
            logger.debug("Creating json from the file")
            pjson = json.loads(f.read())
            logger.debug("json created from the file")
            for item in pjson:
                logger.debug(f"item = {item}")
                for lang in item['languages']:
                    logger.debug(f"lang = {lang}")
                    try:
                        langCount[lang] = langCount[lang] + 1
                        logger.debug(f"{lang} lang found in langCount, increasing count")
                    except KeyError:
                        logger.debug(f"{lang} lang not found in langCount dictionary, adding key and setting count = 1")
                        langCount[lang] = 1
        logger.debug(f"Sorting dictionary langCount")
        langCount = sorted(langCount.items(), key=lambda item: item[1], reverse=True)
        logger.debug(f"Sorting dictionary langCount complete")
    except Exception as e:
        logger.exception(e)
    else:
        logger.info(f"Result --> \n{langCount[:outputno]}")
        return langCount[:outputno]
    finally:
        logger.info("End mostSpokenLang function.")

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def mostPopulatedCountries(fname, count):
    logger.info("Start mostPopulatedCountries function")
    countryPopulation = []
    try:
        logger.debug(f"Reading file {fname}")
        with open(fname, 'rt', encoding='utf-8') as f:
            logger.debug("Creating json from the file")
            pjson = json.loads(f.read())
            logger.debug("json created from the file")
            for item in pjson:
                logger.debug(f"item = {item}")
                countryPopulation.append({'Country': item['name'], 'Population': item['population']})
                logger.debug(f"countryPopulation = {countryPopulation}")
        logger.debug(f"Sorting dictionary langCount")
        countryPopulation = sorted(countryPopulation, key=lambda item: item['Population'], reverse=True)
        logger.debug(f"Sorting dictionary langCount complete")
    except Exception as e:
        logger.exception(e)
    else:
        logger.info(f"Result --> \n{countryPopulation[:count]}")
        return countryPopulation[:count]
    finally:
        logger.info("End mostPopulatedCountries function")

# Extract all incoming email addresses as a list from the email_exchange_big.txt file
def findEmails(fname) -> list:
    logger.info("Start findEmails function")
    email_lt = []
    try:
        logger.debug(f"Reading file {fname}")
        with open(fname) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if not line.startswith("From:"):
                    continue
                else:
                    line = line.strip()
                    logger.debug(f"Strip line -> {line}")
                    line_lt = line.split()
                    logger.debug(f"After split line -> {line_lt}")
                    email = line_lt[1]
                    logger.debug(f"email -> {email}")
                    if email_lt.count(email) == 0:
                        logger.debug(f"{email} does not exist in email_lt. Hence appending")
                        email_lt.append(email)
                        logger.debug(f"Appended successfully.")
                    else:
                        logger.debug(f"{email} exist in email_lt.")
    except Exception as e:
        logger.exception(e)
    else:
        logger.info(f"Return --> {email_lt}")
        return email_lt
    finally:
        logger.info("End findEmails function")

# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order.
def findMostCommonWords(file, count: int) -> list:
    logger.info("Start findMostCommonWords function")
    try:
        with open(file, 'rt', encoding="utf-8") as f:
            text = f.read()
            words = re.findall(r'\b\w+\b', text.lower())
        
        word_counts = Counter(words)
        return word_counts.most_common(count)
                
    except Exception as e:
        logger.exception(e)
    finally:
        logger.info("End findMostCommonWords function")
