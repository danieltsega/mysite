from django.urls import path
from . import views

# Provide the app name
app_name = 'blog'

# Url patterns for each view
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
