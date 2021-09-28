from django.http import HttpResponse
from django.utils.html import escape
from django.views import View
from django.shortcuts import render

msg = '{ "game1": [ ["e2", "e4"], ["e7", "e5"] ] }'
def some(request):
    return HttpResponse(msg, content_type='application/json')

class RestMainView(View) :
    def get(self, request, guess):
        f = ['1', '2', '3']
        ctx = {'guess' : int(guess),
               'numbers' : f,
               'zap' : '<b>bold</b>'
                }
        return render(request, 'polls/cond.html', ctx)

class RestMainView2(View) :
    def get(self, request):
        ctx = { 'zap' : '<b>bold</b>' }
        return render(request, 'polls/cond2.html', ctx)
