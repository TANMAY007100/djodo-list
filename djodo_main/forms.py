from django.forms import Form, CharField

class TodoItem(Form):

    todo = CharField(max_length=500, required=True)

    class Meta:
        db_table = "todo_item"
        verbose_name = "todo item"
        verbose_name_plural = "todo items"