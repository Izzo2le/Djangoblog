from django.urls import path
from blog import views

urlpatterns = [
    ...
    path('blog/', views.hello_blog, name='hello_blog'),
]