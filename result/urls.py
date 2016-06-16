from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^main/$',views.by_total_marks,name="main"),
url(r'^main/(?P<order>[0-9]+)$',views.by_total_marks,name="main"),
url(r'^external/$',views.by_external_marks,name="external"),
url(r'^internals/$',views.by_internal_marks,name="internal"),
url(r'^internals/(?P<order>[0-9]+)$',views.by_internal_marks,name="internals"),
url(r'^(?P<rno>[0-9]+)/$',views.profile,name="profile"),
]