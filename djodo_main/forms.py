from django.forms import Form, CharField, TextInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class TodoItem(Form):

    todo = CharField(max_length=500, required=True)

    class Meta:
        db_table = "todo_item"
        verbose_name = "todo item"
        verbose_name_plural = "todo items"


class SignInForm(AuthenticationForm):

    username = UsernameField(label="Email ID / Username",
                             widget=TextInput(attrs={'autofocus': True}))