from django.contrib.auth.forms import UserCreationForm



#SignupForm
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #mailaddressの追加
        fields = ('username','email')