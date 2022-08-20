from django.urls import path, re_path
from hello.views import hello_world, hello_china, hello_html, article_list, search, render_str, render_html

urlpatterns = [
    path('world/', hello_world),
    path('china/', hello_china),
    path('html/', hello_html),
    # path('article/<int:month>/', article_list)
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list),
    path('search/', search),
    path('render/str/', render_str),
    path('render/html/', render_html)
]
