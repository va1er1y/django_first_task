from django.contrib import admin
from .models import Tag, Scope, Article
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                i += 1
            else:
                continue
        if i == 0:
            raise ValidationError('Выберите главную тему')
        elif i > 1:
            raise ValidationError('Главной темой может быть только одна')
        return super().clean()
class ScopeInline(admin.TabularInline):
    model = Scope
    extre = 0
    formset = ScopeInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    tage_name = ['id','name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
       inlines = [ScopeInline]
