# encoding: utf-8

import os
import time 
import logging
import logging.handlers
from django.core.management.base import BaseCommand, CommandError
from jarvis.extern.jabberbot import JabberBot, botcmd
from jarvis.models import Service, Message, Sender
from jarvis import settings

LOG_FILENAME = os.path.join(settings.PROJECT_PATH,"jarvis.log")
AUTH_CONF    = os.path.join(settings.PROJECT_PATH,"auth.conf")

class JarvisBot(JabberBot):

    sender_cache = {}
    
    def __init__( self, service, res = None):
        self.service = service
        super(JarvisBot, self).__init__( service.jid(), service.password, res)
        self._set_logger()

    def get_sender(self,jid):
        username = jid.getStripped()
        if username in self.sender_cache:
            self.log.info("cached sender %s" % jid)
            return self.sender_cache.get(username)
        else:
            sender, created = Sender.objects.get_or_create(username=username, service=self.service)
            self.sender_cache[username] = sender
            self.log.info("new sender %s" % jid)
            return sender


    def simple_message_handler(self,jid,text,username,props):
        self.log.info("<%s> %s" % (username,text))
        sender = self.get_sender(jid)
        message = Message()
        message.jid = jid
        message.sender = sender
        message.text = text
        message.props = unicode(props)
        message.save()
        
        
    def _set_logger(self):
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        chandler = logging.StreamHandler()
        chandler.setFormatter(formatter)
        self.log.addHandler(chandler)
        self.log.setLevel(logging.INFO)
        
        
class Command(BaseCommand):
    help = 'Launch Jarvis daemon'

    def handle(self, *args, **options):
        try:
            service = Service.objects.get()
        except Service.DoesNotExist:
            jid      = raw_input("jabberid: ")
            password = raw_input("password: ")
            username, domain = jid.split("@",1)
            service = Service(username=username,password=password,domain=domain)
            service.save()
        
        jb = JarvisBot(service)
        jb.serve_forever()

        
