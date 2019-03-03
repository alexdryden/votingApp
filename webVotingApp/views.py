from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import View

from .models import (
    Judge,
    Author,
    Year,
)


class AuthorList(View):
    def get(self, request):
        return render(
            request,
            'votingAppHTML/authorList.html',
            {'author_list': Author.objects.all()}
        )


class JudgeList(View):
    def get(self, request):
        return render(
            request,
            'votingAppHTML/judgeList.html',
            {'judge_list': Judge.objects.all()}
        )


class JudgeDetail(View):
    def get(self, request, pk):
        judge = get_object_or_404(
            Judge,
            pk=pk
        )

        return render_to_response(
            'votingAppHTML/judgeDetail.html',
            {'judge': judge}
        )


class AuthorDetail(View):
    def get(self, request, pk):
        author = get_object_or_404(
            Author,
            pk=pk
        )

        return render_to_response(
            'votingAppHTML/authorDetail.html',
            {'author': author}
        )
