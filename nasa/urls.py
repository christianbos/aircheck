from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^main/',
        include('main.urls', namespace="main")),

    url(r'^measurer/',
        include('measurer.urls', namespace="measurer")),

]
