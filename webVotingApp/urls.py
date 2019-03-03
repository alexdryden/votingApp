from django.urls import path

from webVotingApp.views import AuthorList, JudgeList, MemberDetail, CandidateDetail

urlpatterns_dict = {'authors': AuthorList,
                    'judges': JudgeList,
                    'member/<int:pk>': MemberDetail,
                    'candidate/<int:pk>': CandidateDetail,
                    }

urlpatterns = [path(key + '/',
                    value.as_view(),
                    name='webVotingApp' + key + 'list_urlpattern')
               for key, value in urlpatterns_dict.items()]
