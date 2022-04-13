from django.shortcuts import render, redirect
from HomePage.models import Post
from HomePage.form import PostForm
# Create your views here.


def index(request):
  posts = Post.objects.all()
  if request.method == 'POST':
    form =  PostForm(request.POST)
    if form.is_valid():
      post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
      post.save()
      return redirect('HomePage:home')

  create_post = PostForm()
  return render(request,'index.html' ,{
    'posts': posts,
    'create':create_post,
  })