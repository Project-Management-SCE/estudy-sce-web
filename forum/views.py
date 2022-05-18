from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from forum.form import PostForumForm, CommentForm
from forum.models import Post, Comment
from accounts.models import User



class forumView(View):
    def get(self, request):
        form_post = PostForumForm()
        form_comment = CommentForm()
        all_posts = Post.objects.prefetch_related("comment_set")
        return render(
            request,
            "fourm.html",
            {
                "form_post": form_post,
                "all_posts": all_posts,
                "form_comment": form_comment,
            },
        )
