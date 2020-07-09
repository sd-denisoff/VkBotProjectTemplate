import os
import shutil

from config import application, db, manager


@manager.command
def runserver():
    application.config['DOMAIN'] = 'localhost:5000/'
    application.run(host='localhost', port=5000, debug=True)


@manager.command
def db_delete():
    if os.path.exists('migrations'):
        shutil.rmtree('migrations')
    if os.path.exists('database.db'):
        os.remove('database.db')


@manager.command
def db_reset():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
