from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm as AllAuthSignupForm
from django.contrib.auth.models import Group
from users.models import Instructor, Student

from utils.constants import UserTypes

User = get_user_model()


class SignupForm(AllAuthSignupForm):
    user_type = forms.ChoiceField(
        choices=UserTypes.choices,
        required=True,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'user_type', 'password1', 'password2')

    def save(self, request):
        user = super().save(request)
        user_type = int(self.cleaned_data['user_type'])

        group_name = None
        if user_type == UserTypes.INSTRUCTOR:
            group_name = UserTypes.INSTRUCTOR.label
            Instructor.objects.create(user=user)
        elif user_type == UserTypes.STUDENT:
            group_name = UserTypes.STUDENT.label
            Student.objects.create(user=user)

        # Add to group if valid group_name
        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
        return user

