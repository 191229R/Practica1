from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate

# Create your views here.

class LandingClass(View):
    template_ok = 'Landing/Landing.html'
    def get(self, request, *args, **kargs ):
        return render(request, self.template_ok,{})


