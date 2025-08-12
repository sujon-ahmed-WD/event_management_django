
from django.urls import path
from users.views import sign_up,sign_in,logout_view,activate_user,admin_dashboard,assign_role,create_group,group_list,delete_group,ProfileView,ChangePassword,CustomPasswordResetView,CustomPasswordConfirmResetView,EditProfileView
from django.contrib.auth.views import LogoutView ,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('register/',sign_up, name='sign_up'),
    path('sign-in/',sign_in,name="sign_in"),
    path('logout/', logout_view, name='logout'),
    path('activate/<int:user_id>/<str:token>/',activate_user),
    path('admin/dashboard/',admin_dashboard,name='admin_dashboard'),
    path('admin/<int:user_id>/assign-role/',assign_role,name="assign-role"),
    path('admin/create-group/',create_group,name="create-group"),
    path('admin/group-list/',group_list,name='group_list'),
    path('admin/delete-group/<int:group_id>/',delete_group,name='delete_group'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('password-change/',ChangePassword.as_view(),name='password_Change'),
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
    name='password-change'),
    path('password-reset/',CustomPasswordResetView.as_view(),name='password-reset'),
    path('password-reset/confirm/<uidb64>/<token>/',CustomPasswordConfirmResetView.as_view(),name='password_reset_confirm'),
    path('edit-profile/',EditProfileView.as_view(),name='update-profile')
    
    
]