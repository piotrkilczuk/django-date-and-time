from django import urls
from django.views import generic

from example import models, forms


class ReminderCreateView(generic.CreateView):
    template_name = "reminder_create.html"
    form_class = forms.ReminderForm

    def get_success_url(self):
        return urls.reverse("reminder_detail_view", args=(self.object.pk,))


class ReminderDetailView(generic.DetailView):
    template_name = "reminder_view.html"
    model = models.Reminder
