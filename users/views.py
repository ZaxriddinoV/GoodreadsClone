from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views import View

from users.forms import CreatUsersForm,UserUpdateForm

# Create your views here.

class RegisterViews(View):
    def get(self, request):
        creat_forms = CreatUsersForm
        context={
            "form":creat_forms
        }
        return render(request, "users/register.html",context)


    def post(self, request):
        creat_forms = CreatUsersForm(data=request.POST)

        if creat_forms.is_valid():
            creat_forms.save()
            return redirect('users:login')
        else:
            context = {
                "form": creat_forms
            }
            return render(request, "users/register.html", context)



class LoginViews(View):
    def get(self,request):
        login_form = AuthenticationForm()
        context = {
            'login_form':login_form
        }

        return render(request, "users/login.html",context)
    def post(self,request):

        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request,user)
            messages.info(request,'Successfull')
            return redirect('book:books')

        else:
            return render(request, "users/login.html", {'login_form': login_form})

class LogoutView( LoginRequiredMixin ,View):
    def get(self,request):
        logout(request)
        messages.info(request, "Akauntdan chiqish muvofaqqiyatli boladi")
        return redirect('landing_page')

class ProfileView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return render(request,'users/profile.html', {'user':request.user})
class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self,reqest):
        update_form = UserUpdateForm(instance=reqest.user)
        context = {'update':update_form}
        return render(reqest,'users/profile_edit.html',context)
    def post(self,request):
        update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if update_form.is_valid():
            update_form.save()
            messages.success(request,"Successfull update profile")
            return redirect('users:profile')


        return render(request,'users/profile_edit.html',{'form':update_form})




