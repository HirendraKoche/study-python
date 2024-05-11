import logging.config
import yaml

def setupLog():
    try:
        with open("log_config.yml", "r") as cf:
            config = yaml.safe_load(cf)
            logging.config.dictConfig(config)
    except Exception as e:
        print(e)