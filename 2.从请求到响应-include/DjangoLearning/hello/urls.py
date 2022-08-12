from django.urls import path
from hello.views import hello_world, hello_china

urlpatterns = [
    path('world/', hello_world),
    path('china/', hello_china)
]
