from django.contrib.auth.decorators import login_required
from jarvis.utils.rendering import render_to_response
from jarvis.models import Service

@login_required
def index(request):
    service_list = Service.objects.all()
    return render_to_response(request,"index.html",locals())