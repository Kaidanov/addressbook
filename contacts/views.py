from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Contact
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist


# A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used:
#
# You want to provide a lot of optional features for a class.
# You want to use one particular feature in a lot of different classes.
class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


# ContactOwnerMixin overrides the get_object() method, which is
# responsible for getting the object for a view to operate on.
# If it can’t find one with the specified primary key and owner,
# it raises the PermissionDenied exception.

# Note This implementation will return HTTP 403 (Forbidden) whenever it
# cannot find the a Contact with the requested ID and owner.
# This will mask legitimate 404 (Not Found) errors.
# We’ll use the ContactOwnerMixin in all of our views.

# Note that the order of inheritance is important:
# the superclasses (LoggedInMixin, ContactOwnerMixin, DetailView)
# will be checked in the order listed for methods.
# By placing LoggedInMixin first, you’re guaranteed that by the time execution reaches
# ContactOwnerMixin and DetailView, you have a logged in, authenticated user.
class ContactOwnerMixin(object):

    def get_object(self, queryset=None):
        """Returns the object the view is displaying.

        """
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied

        return obj


# # test connectivity issue
class ListContactView(LoggedInMixin, generic.ListView):
    model = Contact
    template_name = 'contact_list.html'
    fields = '__all__'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


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

class ContactView(LoggedInMixin, ContactOwnerMixin, generic.DetailView):
    model = Contact
    template_name = 'contact.html'
    fields = '__all__'
# class ContactView(generic.DetailView):
#     model = Contact
#     template_name = 'contact.html'
#     fields = '__all__'


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
