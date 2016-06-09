from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^modificar_formulas/', include('modificar_formulas.urls')),
	url(r'^admin/', admin.site.urls),
]
