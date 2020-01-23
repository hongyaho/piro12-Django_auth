# 재정의 해주고 싶으면 하는거
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    pass
