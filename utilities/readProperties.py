import configparser
import os


config = configparser.RawConfigParser()
config.read(os.path.dirname(os.path.dirname(__file__))+'/Configurations/config.ini')


class ReadConfigProperty():
    @staticmethod
    def getapplicationURL():
        return config.get("commoninfo", "base_URL")

    @staticmethod
    def getusername():
        return config.get("commoninfo", "username")

    @staticmethod
    def getpassword():
        return config.get("commoninfo", "password")


