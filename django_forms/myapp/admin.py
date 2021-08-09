from myapp.forms import SnippetForm
from django.contrib import admin
from .models import Snippet

admin.site.register(Snippet)