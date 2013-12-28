# -*- coding: utf-8 -*-

from django import forms

class SummonerSearchForm(forms.Form):
	summoner_name = forms.CharField(max_length=32)