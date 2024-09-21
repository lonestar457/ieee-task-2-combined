
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from users import views as users_views
from tickets import views as tickets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('myshk.urls')),
    path('register/',users_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',users_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/',users_views.profile, name='profile'),

    path ('ticket_details/',tickets_views.ticket_details, name= 'ticket_details'),
    path ('create_ticket/',tickets_views.create_ticket, name= 'create_ticket'),
    path ('all_tickets/',tickets_views.all_tickets, name= 'all_tickets'),
    path ('ticket_queue/',tickets_views.ticket_queue, name= 'ticket_queue'),
    path ('accept_ticket/',tickets_views.accept_ticket, name= 'accept_ticket'),
    path ('close_ticket/',tickets_views.close_ticket, name= 'close_ticket'),
    path ('workspace/',tickets_views.workspace, name= 'workspace'),
    path ('update_ticket/',tickets_views.update_ticket, name= 'update_ticket')]
