from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect, render, resolve_url
from .forms import SignupForm

'''
# 회원가입 - 함수 기반
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # 이때가 딱! 회원가입 하고 유저 객체 만들어진 때
                                # 여기서 로그인 처리하면 회원가입하자마자 로그인 되게 되겠죠?
            auth_login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form':form
    })
'''

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())


#회원가입 - 클래스 기반
signup = SignupView.as_view()



@login_required
def profile(request):
    request.user
    return render(request, 'accounts/profile.html')