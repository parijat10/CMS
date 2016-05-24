from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/status/main/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['username']=username
                return HttpResponseRedirect('/status/main/')
            else:
                return render_to_response('authorize/index.html', {'error': 'Your RobotCMS account is disabled.'}, context)
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('authorize/index.html', {'error': 'Invalid login details supplied.'}, context)
    else:
        return render_to_response('authorize/index.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
