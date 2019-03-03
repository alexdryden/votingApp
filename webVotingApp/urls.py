from django.urls import path

from webVotingApp.views import AuthorList, JudgeList, JudgeDetail, AuthorDetail

urlpatterns_dict = {'authors': AuthorList,
                    'judges': JudgeList,
                    'judge/<int:pk>': JudgeDetail,
                    'author/<int:pk>': AuthorDetail,
                    }

urlpatterns = [path(key + '/',
                    value.as_view(),
                    name='webVotingApp' + key + 'list_urlpattern')
               for key, value in urlpatterns_dict.items()]
