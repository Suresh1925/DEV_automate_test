import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class Readconfig:
    @staticmethod
    def getapplicationurl():
        url = config.get('common info', 'URL')
        return url

    @staticmethod
    def getusername():
        login_username = config.get('common info', 'Username')
        return login_username

    @staticmethod
    def getpassword():
        login_password = config.get('common info', 'Password')
        return login_password
