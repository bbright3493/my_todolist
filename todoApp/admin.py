from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from todoApp.models import Todo




class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'todo', 'priority', 'flag', 'pubtime')
    list_filter = ('pubtime',)
    ordering = ('-pubtime',)


admin.site.register(Todo, TodoAdmin)