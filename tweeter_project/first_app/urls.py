from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	#path('formpage/', views.form_name_view, name='form_name'),
    path('formuserpage/', views.form_user_view, name='form_user'),
	]
