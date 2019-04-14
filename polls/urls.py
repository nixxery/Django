from django.urls import path

from . import views
urlpatterns = [
    path('', views.Index, name='index'),
    path('fun/', views.fun, name='fun'),
    path('extrafun/', views.extrafun, name='extrafun'),
]
