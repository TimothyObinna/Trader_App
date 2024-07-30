
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


class ForgotPassword(View):
  def get(self, request):
    messages.success(request, 'Proceed to reset your password')
    return render(request, 'user/page-forgot-password.html')

  def post(self, request):
    email = request.POST.get('email')

    try:
      user = User.objects.get(email=email)
      if not user.is_emailverified:
        messages.error(request, 'Email not verified')
        return redirect('reverifyit')
    except User.DoesNotExist:
      messages.error(request, 'User with this email address does not exist')
      return redirect('signup')

    # Generate a one-time use token for password reset
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    # Construct the password reset link
    reset_link = f"http://{request.get_host()}{reverse('reset-password', args=(uid, token))}".strip('/')

    # Send the password reset link to the user's email
    send_mail(
      'Password Reset',
      f'Use this link to reset your password: {reset_link}',
      'emchadexglobal@gmail.com',
      [email],
      fail_silently=False,
    )
    messages.success(request, 'Password reset link sent!')
    return render(request, 'user/page-forgot-password.html')
    



class PasswordReset(View):
    def get(self, request, uidb64, token):
        try:
            # Decode the user ID from base64
            uid = force_str(urlsafe_base64_decode(uidb64))
            # Get the user based on the decoded ID
            user = User.objects.get(pk=uid)

            # Check if the token is valid for the user
            if default_token_generator.check_token(user, token):
                # Render the password reset form
                messages.success(request, 'Reset your password here')
                return render(request, 'user/page-reset-password.html', {'validlink': True, 'uidb64': uidb64, 'token': token})
            
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, MultipleObjectsReturned):
            pass

        # If the link is invalid,
        messages.error(request, 'Reset-link is used. Add your email for a new one.') 
        return render(request, 'user/page-forgot-password.html')
    


    def post(self, request, uidb64, token):
        # Handle the form submission to set a new password
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
 
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'user/page-reset-password.html')

        # Set the new password
        user.set_password(password)
        user.save()

        # Redirect to the login page
        messages.success(request, 'Password reset success!  Login')
        return redirect('login')

