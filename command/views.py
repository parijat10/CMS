from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
import os, math




import socket, select, string, sys
 
def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()
 
#main function

host = ''	
port = 5000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
 
# connect to remote host
try :
    s.connect((host, port))
except :
    print 'Unable to connect'
    sys.exit()
 
print 'Connected to remote host. Start sending messages'

 

# import django_socketio

#Create your views here.
# 
@login_required
def index(request):
	context = RequestContext(request)
	return render_to_response('command/index.html', {'username':request.user.username}, context)

@login_required
def control(request):
	context = RequestContext(request)
	return render_to_response('command/control.html', {'username':request.session['username']}, context)

def moveBot(request):
	context = RequestContext(request)
	socket_list = [sys.stdin, s]
	if(request.GET['dir'] == 'controlBotU'):
		s.send("2,up")
	elif(request.GET['dir'] == 'controlBotD'):
		s.send("2,down")
	elif(request.GET['dir'] == 'controlBotL'):
		s.send("2,left")
	else:
		s.send("2,right")
	return HttpResponse(request.GET['dir'])

def sendCoord(request):
    context = RequestContext(request)
    coordinates = [request.REQUEST['xcoord'], request.REQUEST['ycoord']]
    os.system('rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '+"\'["+coordinates[0]+", "+coordinates[1]+", 0]\' \'[0, 0, 0]\'")
    return HttpResponse(coordinates)
