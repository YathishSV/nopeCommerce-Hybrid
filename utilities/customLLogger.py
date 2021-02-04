import logging


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\SG0305099\\PycharmProjects\\nopeCommerce-Hybrid\\Logs\\automation.log" ,
                            format="%(asctime)s- %(levelname)s: %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S",
                            level=logging.INFO)
        logger = logging.getLogger()
        return logger