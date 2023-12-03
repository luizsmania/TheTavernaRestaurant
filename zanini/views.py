from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm, ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


@login_required(login_url='login')
def book_table(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Extracts form data and checks table availability before making a reservation.
            table_size = form.cleaned_data.get("table_size")
            booking_time = form.cleaned_data.get("booking_time")
            date = form.cleaned_data.get("date")

            if Reservation.check_table_availability(table_size, booking_time, date):
                # Creates a reservation if the table is available and the user hasn't already made a reservation.
                reservation = Reservation(date=date, table_size=table_size, booking_time=booking_time)
                if not Reservation.objects.filter(user=request.user).exists():
                    reservation.user = request.user
                    reservation.save()
                    messages.success(request, 'Table booked successfully')
                    return redirect('user_page')
                messages.success(request, 'Sorry, you can just make one reservation at a time.')
                return redirect('book_table')
            messages.success(request, 'Sorry, the tables are full for this date and time.')
            return redirect('book_table')
    return render(request, 'book_table.html', {'form': form})


@login_required(login_url='login')
def delete_reservation(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.delete()
    messages.success(request, 'Reservation canceled successfully')
    return redirect('user_page')


@login_required(login_url='login')
def update_reservation(request, id):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Updates reservation details after checking table availability for the new date and time.
            reservation = Reservation.objects.get(id=id)
            reservation.table_size = form.cleaned_data.get("table_size")
            reservation.booking_time = form.cleaned_data.get("booking_time")
            reservation.date = form.cleaned_data.get("date")

            if Reservation.check_table_availability(reservation.table_size, reservation.booking_time, reservation.date):
                reservation.save()
                messages.success(request, 'Reservation updated successfully')
                return redirect('user_page')
            messages.success(request, 'Sorry, the tables are full for this date and time.')
    return render(request, 'book_table.html', {'form': form})


@login_required(login_url='login')
def user_page(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'user_page.html', {'reservations': reservations})


@login_required(login_url='login')
def menu_items(request):
    return render(request, 'menu_items.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in.')
                return redirect('user_page')
    form = LoginForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Creates a new user account, logs them in, and redirects to the user page.
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'You have signed up successfully.')
            return redirect('user_page')
        else:
            return render(request, 'register.html', {'form': form})
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, "The user is deleted")
    return redirect('home')