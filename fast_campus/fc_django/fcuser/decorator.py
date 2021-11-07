from django.http import request
from django.shortcuts import redirect


def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get("user")
        if user is None or not user:
            return redirect('/')
        print("Login required ", user)
        return function(request, *args, **kwargs)
    return wrap
