from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from aradhana import views
import aradhana.urls
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include(aradhana.urls)),
    #url(r'^db', hello.views.db, name='db'),
    
]
