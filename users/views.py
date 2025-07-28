from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required,user_passes_test

# import user

from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator

from users.forms import LoginForm, RegisterForm, AssignRoleForm, create_from


# Create your views here.

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.is_active = False

            user.save()

            messages.success(
                request, "A confirmation mail has been sent. Please check your email."
            )

            return redirect("sign_in")

        else:
            print("form is not valid ")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    return render(request, "registration/login.html", {"form": form})

# @login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("sign_in")
          

def activate_user(request, user_id, token):
    try:
        print(f"Received user_id={user_id},token={token}")
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            print("Token valid.Activating user....")
            user.is_active = True
            user.save()
            return redirect("sign_in")
        else:
            print("Invalid token")
            return HttpResponse("Invalid Id or token")
    except User.DoesNotExist:
        print("User not found")
        return HttpResponse("User not found")

@user_passes_test(is_admin,login_url='no-permission')
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, "admin/dashboard.html", {"users": users})

@user_passes_test(is_admin,login_url='no-permission')
def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm()

    if request.method == "POST":
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get("role")
            user.groups.clear()
            user.groups.add(role)
            messages.success(
                request, f"User{user.username} has been assigned to the {role.name}"
            )
            return redirect("admin_dashboard")

    return render(request, "admin/assign_role.html", {"form": form})

user_passes_test(is_admin,login_url='no-permission')
def create_group(request):
    if request.method == "POST":
        form = create_from(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group{group.name} has been successfully")
            return redirect("create-group")
    else:
        form=create_from()
    return render(request, "admin/create_group.html", {"form": form})

user_passes_test(is_admin,login_url='no-permission')
def delete_group(request, group_id):
    del_group = get_object_or_404(Group, id=group_id)
    del_group.delete()
    return redirect('group_list')

def group_list(request):
    groups=Group.objects.all()
    return render(request,'admin/group_list.html',{'groups':groups})