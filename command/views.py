from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
import os, math

import django_socketio

#Create your views here.

@login_required
def index(request):
	context = RequestContext(request)
	return render_to_response('command/index.html', {'username':request.user.username}, context)

def test(request):
	return render_to_response('command/test.html')

@login_required
def control(request):
	context = RequestContext(request)
	return render_to_response('command/control.html', {'username':request.session['username']}, context)

def moveBot(request):
	context = RequestContext(request)
	if(request.REQUEST['dir'] == 'controlBotU'):
		django_socketio.broadcast_channel("Up", "channel1")
	elif(request.REQUEST['dir'] == 'controlBotD'):
		django_socketio.broadcast_channel("dowm", "channel1")
	elif(request.REQUEST['dir'] == 'controlBotL'):
		django_socketio.broadcast_channel("left", "channel1")
	else:
		django_socketio.broadcast_channel("Right", "channel1")
	return HttpResponse(request.REQUEST['dir'])

def sendCoord(request):
    context = RequestContext(request)
    coordinates = [request.REQUEST['xcoord'], request.REQUEST['ycoord']]
    os.system('rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '+"\'["+coordinates[0]+", "+coordinates[1]+", 0]\' \'[0, 0, 0]\'")
    return HttpResponse(coordinates)
