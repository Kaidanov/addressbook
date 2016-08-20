from django.conf.urls import patterns, include,url
# from .views import MyView,GreetingView
from django.conf import settings
from django.conf.urls.static import static
from . import views

# urlpatterns = [
#     url(r'^index/$', MyView.as_view()),
#     url(r'^greeting/$', GreetingView.as_view(greeting="G'day")), #initializing the view from url configuration
#     url(r'^$', ListContactView.as_view(), name='contacts-list'),
# ]


urlpatterns = [
    url(r'^index/$', views.MyView.as_view()),
    url(r'^greeting/$', views.GreetingView.as_view(greeting="G'day")),  # initializing the view from url configuration
    url(r'^$', views.ListContactView.as_view(), name='contacts-list'),
    url(r'^new$', views.CreateContactView.as_view(), name='contacts-new'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateContactView.as_view(), name='contacts-edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteContactView.as_view(), name='contacts-delete'),
    url(r'^(?P<pk>\d+)/$', views.ContactView.as_view(), name='contacts-view'),
    url(r'^contact_form/$', views.contact_form),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

