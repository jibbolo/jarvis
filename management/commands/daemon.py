# encoding: utf-8

import os
import time 
import logging
import logging.handlers
from django.core.management.base import BaseCommand, CommandError
from jarvis.extern.jabberbot import JabberBot, botcmd
from jarvis import settings

LOG_FILENAME = os.path.join(settings.PROJECT_PATH,"jarvis.log")
AUTH_CONF    = os.path.join(settings.PROJECT_PATH,"auth.conf")

class JarvisBot(JabberBot):

    def __init__( self, jid, password, res = None):
        super(JarvisBot, self).__init__( jid, password, res)
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        # create console handler
        chandler = logging.StreamHandler()
        chandler.setFormatter(formatter)
        # create file handler
        fhandler = logging.handlers.RotatingFileHandler(LOG_FILENAME)
        fhandler.setFormatter(formatter)
        self.log.addHandler(chandler)
        self.log.addHandler(fhandler)
        self.log.setLevel(logging.INFO)

    def simple_message_handler(self,jid,text,username,props):
        self.log.info("<%s> %s [%s]" % (username,text,props))
        
        
class Command(BaseCommand):
    help = 'Launch Jarvis daemon'

    def handle(self, *args, **options):
        try:
            jid,password = open(AUTH_CONF).read().strip().split()
        except (IOError, ValueError):
            jid      = raw_input("jabberid: ")
            password = raw_input("password: ")
            try:
                open(AUTH_CONF,"w").write("%s %s" % (jid,password))
            except IOError:
                pass
        
        jb = JarvisBot(jid,password)
        jb.serve_forever()

        
