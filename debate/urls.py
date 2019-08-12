from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('debate_list/', views.debate_list, name='debate_list'),
    path('<int:debate_id>/', views.debate_detail, name='debate_detail'),
    path('debate_comment/<int:pk>', views.debate_comment, name='debate_comment'),
    path('agree/<int:debate_id>', views.agree, name="agree"),
    path('disagree/<int:debate_id>', views.disagree, name="disagree"),
]
