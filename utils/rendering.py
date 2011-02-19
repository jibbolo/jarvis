from django.template import RequestContext
from django.shortcuts import render_to_response as orig_render_to_response

def render_to_response(request,*args,**kwargs):
    kwargs['context_instance'] = RequestContext(request)
    return orig_render_to_response(*args,**kwargs)
    