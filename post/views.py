from django.shortcuts import render

from post.models import Post


def index_page(request):
    posts = Post.objects.all()
    return render(request, "index.html", locals())