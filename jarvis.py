#!/usr/bin/python
"""
jarvis.py

Created by Giacomo Marinangeli on 2011-02-18.
Copyright (c) 2011 Forinicom Srl. All rights reserved.
"""

import threading
import time 
import logging
import logging.handlers

from jabberbot import JabberBot, botcmd

LOG_FILENAME = "jarvis.log"

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
        print jid,text,username,props
        self.log.info("%s: %s" % (jid,text))

try:
    JID,PASSWORD = open("auth.conf").read().strip().split()
except (IOError, ValueError):
    JID      = raw_input("jabberid: ")
    PASSWORD = raw_input("password: ")
    try:
        open("auth.conf","w").write("%s %s" % (JID,PASSWORD))
    except IOError:
        pass
        
jb = JarvisBot( JID, PASSWORD)
jb.serve_forever()

