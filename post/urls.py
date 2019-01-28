from django.urls import path
from . import views
app_name = "post"

urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:question_id>/', views.details, name = 'details'),
    path('<int:question_id>/update/', views.update, name = 'update'),
    path('create/', views.create, name = 'create'),
    path('<int:question_id>/comment/', views.update, name = 'comment'),
]
