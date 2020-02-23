from . import views

from django.views.generic import TemplateView
from django.urls import include,path
app_name = 'main'


urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('Review_Post',views.ReviewPost.as_view(),name='review_post'),
    path('Review_Post_Done',views.ReviewPost_done.as_view(),name='review_post_done')
]
