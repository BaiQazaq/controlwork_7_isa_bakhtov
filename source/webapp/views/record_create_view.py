from django.views.generic import CreateView
from django.urls import reverse

from webapp.forms import RecordForm
from webapp.models import Record


class RecordCreate(CreateView):
    template_name = 'record_create.html'
    form_class = RecordForm
    model = Record
    
    def get_success_url(self):
        return reverse('index', kwargs={'pk': self.object.pk})