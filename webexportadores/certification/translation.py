from .models import Certification
from modeltranslation.translator import register, TranslationOptions, translator


class CertificationTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Certification, CertificationTranslationOptions)
