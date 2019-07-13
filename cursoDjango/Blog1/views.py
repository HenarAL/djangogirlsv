from datetime import timedelta

from django.shortcuts import render
from . import models
from django.utils import timezone

# Create your views here.
def post_list(request):
    post = models.Post.objects.filter(created_date__lte=timezone.now(),created_date__gte=(timezone.now() - timedelta(hours=6)))
    return render(request, 'Blog1/post_list.html', {"post":post})