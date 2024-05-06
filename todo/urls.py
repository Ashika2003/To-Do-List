from django.urls import path
from todo import views


urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup,name='signup'),
    path('todo/',views.todo,name='add_task'),
    path('tasks/',views.task,name='tasks'),
    path('update/<int:id>',views.updatetask, name='updatetask'),
    path('delete/<int:id>',views.deletetask, name='deletetask'),
    path('logout/',views.logout_user,name='logout'),
]