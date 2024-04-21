from django.urls import path

from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/register',views.register,name='register'),
    path('all_categories',views.all_categories,name='all_categories'),
    path('category_questions/<int:cat_id>',views.category_questions,name='category_questions'),
    path('submit_answer/<int:cat_id>/<int:quest_id>',views.submit_answer,name='submit_answer'),
    
]
