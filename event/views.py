from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import Event
from .forms import NewEventForm
from company.models import Company


class CompanyEvents(generic.ListView):
    template_name = 'event/company_events.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Event.objects.filter(company=Company.objects.get(user=self.request.user))


class NewEventView(CreateView):
    model = Event
    form_class = NewEventForm

    def form_valid(self, form):
        event = form.save(commit=False)
        event.company = Company.objects.get(user=self.request.user)
        return super(NewEventView, self).form_valid(form)


class EventUpdateView(UpdateView):
    model = Event
    form_class = NewEventForm


class CompanyEvent(generic.DetailView):
    model = Event
    template_name = 'event/company_event.html'


class StudentEvents(generic.ListView):
    template_name = 'event/student_events.html'
    context_object_name = 'list'

    def get_queryset(self):
        l = []
        es = Event.objects.all()
        for x in es:
            xx = CustomEvent(x, x.company)
            l.append(xx)
        return l


class CustomEvent:

    def __init__(self, e, c):
        self.pk = e.pk
        self.name = c.name
        self.cweb = c.website
        self.caddr = c.address + ', ' + c.city + ', ' + c.state + ', ' + c.zipcode
        self.logo = c.logo
        self.title = e.title
        self.address = e.address + ', ' + e.city + ', ' + e.state + ', ' + e.zipcode
        self.date = e.date
        self.time = e.time
        self.website = e.website
        self.desc = e.description


