from .models import About
from modeltranslation.translator import register, TranslationOptions, translator


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(About, AboutTranslationOptions)
