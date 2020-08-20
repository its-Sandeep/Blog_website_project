from django.urls import path
#from . import views
from django.contrib.auth import views as auth_views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView,AddCommentView
from members.views import PasswordChangeView,ShowProfilePageView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article_details"),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('add_category/',AddCategoryView.as_view(),name="add_category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete_post"),
    path('category/<str:cats>/',CategoryView,name="category"),
    path('category_list/',CategoryListView,name="category_list"),
    path('like/<int:pk>',LikeView,name="like_post"),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/',PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name="add_comment"),
    #path('<int:pk>/profile',ShowProfilePageView.as_view(),name='show_profile_page'),
]

 