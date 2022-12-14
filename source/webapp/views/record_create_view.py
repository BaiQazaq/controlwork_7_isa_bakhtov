from django.views.generic import CreateView
from django.urls import reverse_lazy

from webapp.forms import RecordForm
from webapp.models import Record


class RecordCreate(CreateView):
    template_name = 'record_create.html'
    form_class = RecordForm
    model = Record
    success_url = reverse_lazy('index')
    