from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<int:person_id>/', views.person_page, name='person_page'),
    path('history/<int:person_id>/', views.edit_history, name='edit_history'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)