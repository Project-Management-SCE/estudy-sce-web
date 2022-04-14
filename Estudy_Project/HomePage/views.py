from django.shortcuts import render, redirect
from HomePage.models import Post
from HomePage.form import PostForm
from django.views import View
# Create your views here.


class indexView(View):
  def get(self,request):
    posts = Post.objects.all()
    create_post = PostForm()
    return render(request,'index.html' ,{
      'posts': posts,
      'create':create_post,
  })
  def post(self,request):
    form =  PostForm(request.POST)
    if form.is_valid():
      post = Post(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
      post.save()
      return redirect('HomePage:home')
    return redirect('HomePage:home')


class aboutView(View):
  def get(self,request):
    return render(request,"about.html")

def deletePost(request,post_id):
  post = Post.objects.get(pk=post_id)
  post.delete()
  return redirect('HomePage:home')

def updatePost(request,post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('HomePage:home')
    return render(request,'accounts/update.html',{'post':post,'form':form})
