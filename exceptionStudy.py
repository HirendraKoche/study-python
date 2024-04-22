# Learning Exception handling in python.

import logging
from setupLog import setupLog

# enabling logging for exception handling study.
setupLog()
logger = logging.getLogger("study.exception")

def reader(f):
    logger.info("Inside reader function")
    try:
        with open(f, 'r') as file:
            logger.info(f"Reading file : {f}")
            content = file.read()
            logger.info(f"Read complete")
            logger.info(f"Printing content of file : {f}")
            print(content)
            logger.info(f"Printing completed.")
    except Exception as e:
        logger.exception(e, stack_info=True)
    finally:
        logger.info("End reader function")

def main():
    logger.info("Inside main function")
    logger.info("Call reader function")
    reader("./builtInFunction.py")
    logger.info("End main function\n")

main()