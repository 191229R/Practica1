from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DashboardClass(LoginRequiredMixin,View):
    template_oke ='Dashboard/Dashboard.html'
    def get(self, request, *args, **kargs ):
        return render(request, self.template_oke,{})