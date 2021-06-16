from django.contrib import admin
from django.urls import path
from currency.views import hello_world
from currency.views import gen_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('gen_password/', gen_password),

]
