# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Articles
from .models import Comments
from django.utils import timezone
from .forms import CommentsForm
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        articles = Articles.objects.filter()
        comments = Comments.objects.filter()
        return render(request, 'index.html', {'articles': articles,'comments': comments})
#
# def comment_new(request):
#     form = CommentsForm()
#     return render(request, 'comment_edit.html', {'form': form})
def comment_new(request):
    if request.method == "COMMENT":
        form = CommentsForm(request.COMMENT)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentsForm()
    return render(request, 'comment_edit.html', {'form': form})




# def articles_list(request):
#     articles = articles.objects.filter()
#     return render(request, 'BoiBye2017/index.html', {'articles': articles})
# Create your views here.
