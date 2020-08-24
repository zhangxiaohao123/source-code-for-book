from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from .forms import CommentForm


def blog_comment(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name=request.user.nikename
            comment.email=request.user.email
            comment.blog = blog
            comment.save()
            return redirect(blog)
        else:
            comment_list = blog.comment_set.all()
            context = {'blog': blog,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(blog)
