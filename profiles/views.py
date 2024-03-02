from dataclasses import fields
from re import sub
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as fi:
#         for chunk in file.chunks():
#             fi.write(chunk)


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    models = UserProfile
    fields = "__all__"
    success_url = "/profiles"
    def get_queryset(self):
        return UserProfile.objects.all()


class ProfilesView(ListView):
    template_name = "profiles/user_profiles.html"
    models = UserProfile
    context_object_name = "profiles"
    def get_queryset(self):
        return UserProfile.objects.all()

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

    # def post(self, request):
    #     # print(request.FILES["image"])
    #     submit_form = ProfileForm(request.POST, request.FILES)

    #     if submit_form.is_valid():
    #         # store_file(request.FILES["image"])
    #         profile = UserProfile(image=request.FILES["user_image"])
    #         profile.save()
    #         return HttpResponseRedirect("/profiles")

    #     # store_file(request.FILES["image"])
    #     # return HttpResponseRedirect("/profiles")
    #     return render(request, "profiles/create_profile.html", {
    #         "form": submit_form
    #     })
