from django.urls import path
from .views import PersonasView

urlpatterns = [
    path('personas/', PersonasView.as_view(), name='personas_list'),
    path('personas/<int:id>', PersonasView.as_view(), name='personas_process')
]