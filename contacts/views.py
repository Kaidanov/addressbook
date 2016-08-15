from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Contact
from django.core.urlresolvers import reverse


class ListContactView(generic.ListView):
    model = Contact
    template_name = 'contact_list.html'



class CreateContactView(generic.CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context


class UpdateContactView(generic.UpdateView):
    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteContactView(generic.DeleteView):
    model = Contact
    template_name = 'delete_contact.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')


class ContactView(generic.DetailView):
    model = Contact
    template_name = 'contact.html'
    fields = '__all__'





# def hello_world(request):
#     return HttpResponse("Hello, World")


class MyView(generic.View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')


# base view usage
class GreetingView(generic.View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


# override base view usage in a subclass
# the get is used from the parent
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"


