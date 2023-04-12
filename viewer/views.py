from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import CreateView

from viewer.forms import AdForm

LOGGER = getLogger()


class AdCreateView(CreateView):

    template_name = 'form.html'
    form_class = AdForm
    #success_url = reverse_lazy('View_ads')

    def form_invalid(self, form):
        LOGGER.warning('Wprowadzono błędne dane')
        return super().form_invalid(form)