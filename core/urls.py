from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import index, contato

urlpatterns = [
    path('', index),
    path('contato', contato),
#    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index2'),

]