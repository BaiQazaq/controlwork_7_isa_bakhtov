from django.views.generic import ListView
from webapp.models import StatusChoices
from webapp.models import Record


class IndexView(ListView):
    template_name = 'index.html'
    model = Record
    context_object_name = 'records'
    ordering = ('-created_at',)
    # extra_context = {'aaa': 'bbb'}
    queryset = Record.objects.exclude(status=StatusChoices.NOT_ACTIVE)