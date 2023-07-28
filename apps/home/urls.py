# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # path('team', views.teamFun, name='team'),
    path('capture', views.capCv, name='capture'),
    path('audio', views.audio_upload, name='audio'),
    path('cloud',views.cloud_retrieval,name='cloud'),
    path('video', views.video_upload, name='video'),
    path('forum', views.disussion,name='forum'),
    path('buy', views.buy_view, name='buy'),
    path('analysis/<str:id>/', views.get_time, name='analysis'),
    # path('attendance', views.file_upload, name='attendance'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
