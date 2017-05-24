from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context

def index(request):
    # t = get_template('index.html')
    # html = t.render(Context(locals()))
    # return HttpResponse(html)
    ans = ''

    if request.method == 'POST':
        uid = request.POST.get('nickname')
        
        ans = uid

    return render(request, 'index.html', {"ret": ans})
