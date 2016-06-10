from django.conf.urls import url, include
from django.contrib import admin

#from Keepass-Api.api import KeepassResource
from KeepassApi.views import hello_world

#keepass_resource = KeepassResource()

urlpatterns = [
    url(r'^$', hello_world),
#    url(r'^api/', include(keepass_resource.urls)),
    url(r'^admin/', admin.site.urls),
]
