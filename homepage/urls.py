from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('post/<int:post_id>',views.detail, name='detail'),
    path('post/new/', views.post_new, name = 'new'),
    path('post/<int:post_id>/edit',views.post_edit, name='edit'),
    path('post/<int:post_id>/delete', views.post_delete, name='delete'),
    path('post/<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete', views.comment_delete, name="comment_delete"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, name="photo")

