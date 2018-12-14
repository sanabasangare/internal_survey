from django.conf.urls import url
from survey import views

urlpatterns = [
    url(r'^selection/(?P<survey_pk>\d+)/$', views.selection, name='survey_ajax_selection'),
    url(r'^survey/(?P<survey_pk>\d+)/$', views.survey, name='survey'),
    url(r'^result/(?P<survey_pk>\d+)/$', views.result, name='survey_result'),
]
