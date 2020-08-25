from django.urls import path
from django.conf.urls import url
from .views import (
    list_todo_items,
    insert_todo_item,
    delete_todo_item,
    add_record,
    edit,
    change,

    )

app_name = 'records'

urlpatterns = [
    path('delete_todo/<int:todo_id>/', delete_todo_item, name='delete_todo_item'),
    path('edit/<int:todo_id>/', edit, name='edit'),
    path('change/<int:todo_id>/', change, name='change'),



]
