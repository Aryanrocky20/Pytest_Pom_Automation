import logging
import os

class LogGen:

    def loggen(self):
        file_path = os.path.relpath('..\\logs\\automation.log')
        logging.basicConfig(filename=file_path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger