from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import rospy
from std_msgs.msg import String
# Create your views here.
myData=None
def callback(data):
    myData=data.data
    f = open('coordinates', 'w')
    f.write(str(myData))
    f.close()

def read_coordinates(request):
    context = RequestContext(request)
    file_x_y = open('coordinates', 'r')
    x_y = file_x_y.read()
    return HttpResponse(x_y)

@login_required
def index(request):
	context = RequestContext(request)
	return render_to_response('status/index.html', {'username':request.user.username}, context)

@login_required
def main(request):
    context = RequestContext(request)
    rospy.init_node('listener', anonymous=True, disable_signals=True)
    rospy.Subscriber("chatter", String, callback)
    return render_to_response('status/main.html', {'username':request.user.username, 'data': myData}, context)

@login_required
def view(request):
    context = RequestContext(request)
    return render_to_response('status/view.html', {'username':request.user.username}, context)

def getImage(request):
    context = RequestContext(request)
    with open("static/img/capture.jpg", "rb") as f:
        data = f.read()
        imgdata = data.encode("base64")
        return HttpResponse(imgdata)
