from django.urls import path

from . import views

urlpatterns = [
    path('business-card/<int:pk>/', views.UserBusinessCardView.as_view()),
    path('business-card/new/', views.CreateBusinessCardView.as_view()),
    path('sponsors/', views.ThirdPartyListView.as_view()),
    path('sponsors/new/', views.CreateThirdPartyView.as_view()),
]