from .views import BlocListView
from django.urls import path
from .views import  BlocListView, BlocDEtailView,BlocCreateView, BlocEditView, BlocDeleteView


urlpatterns = [
    path('',BlocListView.as_view(), name = 'home'),
    path("post/<int:pk>/", BlocDEtailView.as_view(), name = 'post_detail'),
    path('post/new', BlocCreateView.as_view(), name = 'post_new'),
    path("post/<int:pk>/edit", BlocEditView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlocDeleteView.as_view(), name="post_delete")
]