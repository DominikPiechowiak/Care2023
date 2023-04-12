from django.urls import path
from .views import AdCreateView

urlpatterns = [
    path('ad/create', AdCreateView.as_view(), name='Ad_create'),
    #path('Ad/update/<pk>', AdUpdateView.as_view(), name='Ad_update'),
    #path('Ad/delete/<pk>', AdDeleteView.as_view(), name='Ad_delete')
]
