from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from jarvis.utils.rendering import render_to_response
from jarvis.models import Service,Sender,Message

@login_required
def index(request,sender_id=None):
    service_list = Service.objects.all()
    try:
        sender_id = int(sender_id)
        sender = get_object_or_404(Sender,pk=sender_id)
        message_logs = Message.objects.filter(sender=sender)
    except:
        sender = message_logs = None
    return render_to_response(request,"index.html",locals())