from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Car
from .models import Booking
from .models import Contact
from .forms import ContactForm
from .models import Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView





def home(request):
    cars = Car.objects.filter(is_available=True)
    return render(request, 'fast_cars/home.html', {'cars': cars})

def about(request):
    return render(request, 'fast_cars/about.html', {'title': 'About'})

def testimonials(request):
    context = {
        'testimonials': Review.objects.all(),
        'title': 'Testimonials'
    }
    return render(request, 'fast_cars/testimonials.html', context)

class PostListView(ListView):
    model = Review
    template_name = 'fast_cars/testimonials.html'
    context_object_name = 'testimonials'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Review


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'content']
    success_url = '/testimonials/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content']
    success_url = '/testimonials/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/testimonials/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'fast_cars/car_detail.html', {'car': car, 'title': car.name})


@login_required
def rent_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if car.is_available:
        # Create a booking record for the rented car
        booking = Booking.objects.create(user=request.user, car=car)
        
        # Perform other rental logic if needed
        
        messages.success(request, f"You have successfully rented the {car.name}. Enjoy your ride!")
    # else:
    #     messages.error(request, f"The {car.name} is currently not available for rent.")
    return redirect('fast-cars-home')


@login_required
def booking_history(request):
    user_bookings = Booking.objects.filter(user=request.user)
    rented_cars = [booking.car for booking in user_bookings]
    context = {
        'rented_cars': rented_cars
    }
    return render(request, 'fast_cars/booking_history.html', context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Thank You! Your message has been sent.")
            form = ContactForm() 
    else:
        form = ContactForm()
    return render(request, 'fast_cars/contact_us.html', {'form': form})