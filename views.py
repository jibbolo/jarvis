from django.contrib.auth.decorators import login_required
from jarvis.utils.rendering import render_to_response

@login_required
def index(request):
    return render_to_response(request,"index.html")