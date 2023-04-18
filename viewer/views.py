from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from viewer.models import Advertisement

from viewer.forms import AdForm

LOGGER = getLogger()


class AdCreateView(CreateView):

    template_name = '../Care2023/templates/viewer/form.html'
    form_class = AdForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        LOGGER.warning('Wprowadzono błędne dane')
        return super().form_invalid(form)


class AdsView(ListView):
  template_name = 'adsview.html'
  model = Advertisement

