from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context

def index(request):
    # t = get_template('index.html')
    # html = t.render(Context(locals()))
    # return HttpResponse(html)

    # return render_to_response('index.html',locals())

    ans = ''
    return render(request, 'index.html', {'ret': ans})
    #
    # template = get_template('index.html')
    # return HttpResponse(template.render(request))
