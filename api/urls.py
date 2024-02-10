from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.MessageAll.as_view()),
    path('create/', views.MessageOne.as_view()),
    path('<int:message_id>/delete/', views.MessageOne.as_view()),
    path('<int:message_id>/read/', views.MessageOne.as_view())
]
