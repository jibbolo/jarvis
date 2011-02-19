# encoding: utf-8
import datetime
from django.db import models

class Service(models.Model):
    username = models.CharField(max_length=64,null=False)
    password = models.CharField(max_length=64,null=False)
    domain   = models.CharField(max_length=64,null=False)
    
    def jid(self):
        return "%s@%s" % (self.username,self.domain)
    
    def __unicode__(self):
        return self.jid()

class Sender(models.Model):
    username = models.CharField(max_length=255,null=False,unique=True)
    service = models.ForeignKey(Service, null=False, related_name="users")
    def __unicode__(self):
        return self.username
        
class Message(models.Model):
    jid = models.CharField(max_length=255,null=False)
    date = models.DateTimeField(null=False, default=datetime.datetime.now)
    props = models.CharField(max_length=255,null=True)
    text = models.TextField(null=True)
    sender = models.ForeignKey(Sender, null=False, related_name="messages")

    def __unicode__(self):
        return "[%s] %s" % (self.date, self.sender)
        