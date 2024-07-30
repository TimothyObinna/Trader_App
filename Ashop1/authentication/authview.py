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

class ReverifyOtp(View):
    def get(self, request):

        return render(request, 'user/page-reverify.html')


    def post(self, request):
        
        entered_email = request.POST.get('email')

        # Check if the entered email matches the one in the database
        try:
            user = User.objects.get(email=entered_email, is_emailverified=False)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email address')
            return redirect('reverifyit')

        # Generate new OTP
        new_otp = random.randint(100000, 999999)
        user.otp = new_otp
        user.otp_created_at = timezone.now()
        user.save()

        # Send new OTP
        subject = "New OTP Verification"
        body = f"Your new verification code is: {new_otp}"
        from_email = EMAIL_HOST_USER  # Update with your email host user
        to_email = entered_email
        send_now = send_mail(subject, body, from_email, [to_email])

        if send_now:
            messages.success(request, 'Success!  New OTP sent')
            return redirect('verifyit') 
        else:
            messages.error(request, 'Failed to send new OTP.  Resend again here.')
            return redirect('reverifyit')



class Verify(View):
    def get(self, request):
        return render(request, 'user/page-verify.html')

    def post(self, request):
        entered_otp = request.POST.get('otp')
        try:
            user = User.objects.get(otp=entered_otp, is_emailverified=False)
            if user.otp_created_at and timezone.now() - user.otp_created_at <= timedelta(minutes=2):
                user.is_emailverified = True
                user.save()
                backend = ModelBackend()
                user.backend = f'{backend.__module__}.{backend.__class__.__name__}'
                login(request, user)
                messages.success(request, 'Success!  Create your account here')
                return redirect('registerit')
            else:
                # user.delete()
                messages.error(request, 'OTP is expired.  Resend another one here')
                return redirect('reverifyit')
            
        except User.DoesNotExist:
            messages.error(request, 'User not found, signup')
            return redirect('signup')
            


