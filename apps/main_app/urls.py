
from django.conf.urls import url
from . import views
def test(request):
    print '*****************************'

    print request.POST
    print '*****************************'

urlpatterns = [

   	url(r'^$', views.index),
    url(r'^user/new$', views.newUser),
    url(r'^pet/new$', views.newPet),
    url(r'^user/create$', views.createUser),
    url(r'^user/show/(?P<id>\d+)$', views.showUser),
    url(r'^pet/create$', views.createPet),
    url(r'^user/pet/add$', views.adopt),
    
]
