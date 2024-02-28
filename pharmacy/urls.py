from django.urls import path, include
from pharmacy import views

urlpatterns = [
    path("ping", views.ping, name="admin"),
    path('cure', views.get_all_cures, name='get_all_cure'),
    # path('cure/id/<int:id>/details', views.get_id_cure, name='get_by_id'),
]


