from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListThesisView.as_view()),
    path('my/', views.ListUserThesisView.as_view()),
    path('create/', views.CreateThesisView.as_view()),
    path('<int:pk>/release/', views.ReleaseThesisView.as_view()),
    path('<int:pk>/hide/', views.HideThesisView.as_view()),
    path('<int:pk>/update/', views.UpdateThesisView.as_view()),
    path('<int:pk>/review/', views.CreateThesisReviewView.as_view()),
]