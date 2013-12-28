# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^summoner/search$', views.SummonerSearchView.as_view(), name='summoner.search'),
    url(r'^summoner/(?P<summoner_id>\w+)$', views.SummonerView.as_view(), name='summoner'),
)
