from django.shortcuts import render, redirect
from django.views import View
from YouTube.models import YouTube

class SearchVideoView(View):
    def get(self, request):
        YouTube.objects.all().delete()
        return render(request, "youtube.html")
