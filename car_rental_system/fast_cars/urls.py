from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path('', views.home, name='fast-cars-home'),
    path('about/', views.about, name='fast-cars-about'),
    path('testimonials/', PostListView.as_view(), name='fast-cars-testimonials'),
    path('testimonials/<int:pk>/', PostDetailView.as_view(), name='testimonial-detail'),
    path('testimonials/<int:pk>/update', PostUpdateView.as_view(), name='testimonial-update'),
    path('testimonials/<int:pk>/delete', PostDeleteView.as_view(), name='testimonial-delete'),
    path('testimonials/new/', PostCreateView.as_view(), name='testimonial-create'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('rent/<int:car_id>/', views.rent_car, name='rent_car'),
    path('history/', views.booking_history, name='booking_history'),
    path('contact/', views.contact_us, name='contact_us'),
]