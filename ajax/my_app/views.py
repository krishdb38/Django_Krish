from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import FriendForm
from .models import Friend




# Create your views here.


def indexView(request):
    form = FriendForm() #
    friends = Friend.objects.all()
    context = {'form': form, 'friends' : friends} 
    return render(request,'my_app/index.html' , context) 

def postFriend(request):
    if request.is_ajax  and request.method == 'POST':
        form = FriendForm(request.POST)
        
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in Json 
            ser_instance = serializers.serialize('json' , [instance, ])
            # send to Client side
            return JsonResponse({'instance' : ser_instance}, status = 200 )
        else:
            return JsonResponse({"error" : form.errors} , status = 400) 
    return JsonResponse({"error" : " "}, status = 400)