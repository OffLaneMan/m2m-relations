from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Tag, Scope


# class TagInline(admin.TabularInline):
#     model = Tag
#     extra = 0
class CleanScope(BaseInlineFormSet):
    def clean(self):
        super().clean()
        i = 0
        for x in self.cleaned_data:
            if x["is_main"] == True:
                i += 1
            if i > 1:
                raise ValidationError("Основной тег может быть только один")


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = CleanScope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # pass
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
