from django.urls import path

from search import views


urlpatterns = [
    path('', views.search_main, name='search_main_page'),
    path('list/<str:title>/', views.movie_list, name="movie_list_page"),
    path('list/<str:title>/<int:number>/', views.review_detail, name='review_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:pk>/', views.review_edit_page, name='review_edit'),
    path('reviews/<int:pk>/del/', views.review_delete, name='review_delete'),
]
