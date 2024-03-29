#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'aditya'
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from ts import db, app
from ts.cron import cron
# from foosball.seed import SeedData

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('cron', cron)
# manager.add_command('seed', SeedData)
manager.add_command("runserver", Server(use_debugger=app.config['SERVER_DEBUG'],
                                        use_reloader=app.config['SERVER_RELOAD'],
                                        host=app.config['SERVER_HOST'],
                                        port=int(app.config['SERVER_PORT']),
                                        threaded=True))


if __name__ == "__main__":
    manager.run()

