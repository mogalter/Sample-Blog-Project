from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# messages.info
# messages.success
# messages.error


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # we create the form with the post data from the form
        if form.is_valid():
            form.save()  # saves the user, password is hashed, etc
            username = form.cleaned_data.get("username")
            messages.success(request, 'Account created for {}!'.format(username))
            return redirect('login')  # specify a name of a view to redirect to
    else:
        form = UserRegisterForm()
    return render(request, 'login_app/register.html', {'form': form})


@login_required
def profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            if not u_form.cleaned_data.get("email"):
                # fill it out with
                print(request.user.email)
                u_form.cleaned_data["email"] = request.user.email
            u_form.save()
            p_form.save()
            messages.success(request, 'Account updated successfully!')
            return redirect("profile")
    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()
    context = {'user_form': u_form,
               'profile_form': p_form
               }
    return render(request, 'login_app/profile.html', context=context)
