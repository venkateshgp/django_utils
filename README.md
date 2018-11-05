# django_utils
Django rest Framework Custom response

This is custome Response template that built on top of HttpResponse, this will be used like below.

Add this function in to your django.app.utils and start using it in your views.

Steps to implement it:
- Copy the code
- Place it in your utils.py file
- Import this utility in to your views.py 
  from utils import custom_resp
- start using it.

Note:
- By refault it will take status as 201, change the same accordingly.
- Django provides a response module in rest framework, which is comprehencive and gives all required functionality, but simple response body is required for small to medium systems.

Lets make it good.
