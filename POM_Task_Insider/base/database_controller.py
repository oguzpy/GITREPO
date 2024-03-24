import configparser
import os
import pymysql
from base.base_functions import BaseFunctions

current_dir = os.path.dirname(os.path.abspath(__file__))
settings_file = os.path.join(current_dir, '..', 'base', 'settings.ini')
config = configparser.ConfigParser()
config.read(settings_file)


def connect():
    return pymysql.connect(host=config.get('DataBaseSettings', 'host'),
                           user=config.get('DataBaseSettings', 'user'),
                           password=config.get('DataBaseSettings', 'password'),
                           database=config.get('DataBaseSettings', 'database'),
                           )


class DataBaseController(BaseFunctions):

    @staticmethod
    def insert_data(case_status, case_report):
        db = connect()
        cursor = db.cursor()
        query = ("INSERT INTO sys.test (casestatus, caseresult) VALUES ('{}', '{}');"
                 .format(case_status, case_report))
        cursor.execute(query)
        db.commit()
        db.close()
