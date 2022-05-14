from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from forum.form import PostForumForm, CommentForm
from forum.models import Post
from accounts.models import User

class forumView(View):
    def get(self, request):
        form_post = PostForumForm()
        return render(
            request,
            "fourm.html",
            {
                "form_post": form_post,
            },
        )
    def post(self, request, user_id):
        form = PostForumForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=user_id)
            post = Post.objects.create(
                user=user, title="", message=form.cleaned_data["message"]
            )
            post.save()
        return redirect("Forum:forum-main")
