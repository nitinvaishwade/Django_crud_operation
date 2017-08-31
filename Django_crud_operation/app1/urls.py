from django.conf.urls import url
from app1.views import index, add_new_record


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_new_record/$', add_new_record, name='add_new_record'),
]