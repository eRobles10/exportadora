from .models import Process
from modeltranslation.translator import register, TranslationOptions, translator


class ProcessTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Process, ProcessTranslationOptions)
