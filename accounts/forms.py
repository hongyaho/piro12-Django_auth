# 재정의 해주고 싶으면 하는거
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email



# 이메일 형식에 맞는지 검사
class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter email format.'
        self.fields['username'].label = ('Email')  # 이렇게 괄호 쳐주면 국제화 기능 되서 언어 변동 가능

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username
        if commit:
            user.save()



'''
class SignupForm(UserCreationForm):
    def clean_username(self):    #각 필드에 대한 validators, clean_field명
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)
        return value
'''