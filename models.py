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
    
class Message(models.Model):
    date = models.DateTimeField(null=False, default=datetime.datetime.now)
    jid = models.CharField(max_length=255,null=False)
    username = models.CharField(max_length=255,null=False)
    props = models.CharField(max_length=255,null=True)
    text = models.TextField(null=True)
    service = models.ForeignKey(Service, null=True, related_name="messages")

    def __unicode__(self):
        return "[%s] %s" % (self.date,self.jid)
        