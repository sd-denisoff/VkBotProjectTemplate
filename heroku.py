from config import application
from manage import db_reset


db_reset()
application.config['DOMAIN'] = ''  # fill it


if __name__ == '__main__':
    application.run()
