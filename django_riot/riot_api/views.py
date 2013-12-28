# -*- coding: utf-8 -*-

from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse
from pyriot.wrapper import PyRiot, NORTH_AMERICA
from django.conf import settings
from forms import SummonerSearchForm
from requests.exceptions import HTTPError

class SummonerSearchView(FormView):
    priot = PyRiot(settings.RIOT_API_KEY)
    template_name = 'summoner_search.html'
    form_class = SummonerSearchForm

    def form_valid(self, form):
        self.summoner = self.priot.summoner_get_by_name(NORTH_AMERICA, form.cleaned_data['summoner_name'])
        return super(SummonerSearchView, self).form_valid(form)

    def get_success_url(self):
        return '/summoner/{0}'.format(self.summoner['id'])
        #return reverse('summoner' kwargs={'summoner_id': self.summoner['id']})


class SummonerView(TemplateView):
    template_name = 'summoner.html'
    priot = PyRiot(settings.RIOT_API_KEY)

    def get_context_data(self, **kwargs):
        context = super(SummonerView, self).get_context_data(**kwargs)
        summoner_id = self.kwargs['summoner_id']
        try:
            summoner = self.priot.summoner_get_by_id(NORTH_AMERICA, summoner_id)
        except HTTPError:
            summoner = None
        context['summoner'] = summoner

        return context