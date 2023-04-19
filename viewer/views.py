from logging import getLogger

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from viewer.models import Advertisement

from viewer.forms import AdForm

LOGGER = getLogger()


class AdCreateView(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    template_name = 'form.html'
    form_class = AdForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        LOGGER.warning('Wprowadzono błędne dane')
        return super().form_invalid(form)


class AdsView(ListView):
    template_name = 'adsview.html'
    model = Advertisement


@login_required
def edit(request, id):
    if id:
        post = get_object_or_404(Advertisement, id=id)
        if post.author != request.user:
            return render(request, "403.html")
        else:
            post = Advertisement(author=request.user)

    if request.method == "POST":
        form = AdForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'You have succesfully updated your post')
            return redirect('index')
    else:
        form = AdForm(instance=post)
    return render(request, 'change_ad.html', {'form': form})