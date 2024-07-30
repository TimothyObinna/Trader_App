from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from Ashop.settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import VendorApplyForm
from django.utils import timezone
from datetime import timedelta

from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.core.exceptions import MultipleObjectsReturned
from django.urls import reverse

from django.contrib.auth.backends import ModelBackend

from product.models import Category, Product, Productimage

User = get_user_model()  # Get the active user model
class VendorApply(View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'User not authenticated')
            return redirect('reverifyit')        
        form = VendorApplyForm()  # Create an empty form instance
        messages.success(request, 'Apply for Vendorship')
        return render(request, 'dash/page-vendor-apply.html', {'form': form})


    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'User not authenticated')
            return redirect('reverifyit')

        # Retrieve current user
        user = request.user

        # Initialize the form with the POST data
        form = VendorApplyForm(request.POST)

        if form.is_valid():
            # Update the user's fields with the form data
            user.business_name = form.cleaned_data['business_name']
            user.location = form.cleaned_data['location']
            user.registration_no = form.cleaned_data['registration_no']
            user.registering_body = form.cleaned_data['registering_body']
            user.phone_number = form.cleaned_data['phone_number']
            user.business_description = form.cleaned_data['business_description']
            user.website_url = form.cleaned_data['website_url']

            # Update user's vendor status
            is_vendor = form.cleaned_data.get('is_vendor')
            if is_vendor:
                user.is_vendor = False
                user.vendor_application_status = 'pending'

            # Save the user instance
            user.save()
            messages.success(request, 'Vendor status, pending. Account created. Login!')
            return redirect('login')
        else:
            messages.warning(request, 'Please fill all required fields')
            return render(request, 'dash/vendor-apply.html', {'form': form})






class VendorPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'User not authenticated')
            return redirect('reverifyit')
        messages.success(request, 'Welcome to your Vendor page')
        return render(request, 'dash/vendor-dashboard.html')
    

    def post(self, request):
        pass


