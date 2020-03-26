from django.shortcuts import render
from django.views.generic import View
#importar metodo de autotenticaion
from django.contrib.auth import authenticate
from django.shortcuts import redirect

#Create your views here.
# def Login(request):
#     return render(request,'Login.html',{})
# def Landing(request):
#     return render(request,'Landing.html',{})


class LandingClass(View):
    templates = 'Landing/Landing.html'
    def get(self, request, *args, **kargs ):
        return render(request, self.templates,{})

class DashboardClass(View):
    template_oke = 'Dashboard/dashboard.html'
    def get(self, request, *args, **kargs ):
        return render(request, self.template_oke,{})

class LoginClass(View):
    templates = 'Login/Login.html'
    template_oke='Dashboard/dashboard.html'

    def get(self, request, *args, **kargs ):
        return render(request, self.templates,{} )

    def post(self, request, *args, **kargs ):
        user_post = request.POST['user']
        password_post = request.POST['password']

        user_sesion = authenticate(username = user_post, password = password_post)

        if user_sesion is not None:
            return redirect('Login:dashboard')
            
            #return render(request, self.template_ok,{} )
        else:
            self.message = 'usuario o cantrasena incorrecto'


        return render(request, self.templates, self.get_context())


        
    def get_context(self):
        return{
            'error':self.message,
        }

        