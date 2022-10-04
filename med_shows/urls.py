from django.urls import path
from . import views

urlpatterns = [
    path('medshows/', views.show_all_med_img, name='medshows'),
    path('medshows/create/', views.add_medshows, name='medshows_create'),
    path('medshows/<int:id>/', views.med_shows_detail, name='medshows_detail'),
    path('medshows/<int:id>/update/', views.show_update, name='medshows_update'),
    path('medshows/<int:id>/delete/', views.delete_medshow, name='medshows_delete')
]
