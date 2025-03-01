from django.conf import settings

def from_settings(request):
    return {
        'ADMIN_NOTICE_SHOW': getattr(settings, 'ADMIN_NOTICE_SHOW', False),
        'ADMIN_NOTICE_FLOAT': getattr(settings, 'ADMIN_NOTICE_FLOAT', True),
        'ADMIN_NOTICE_TEXT': getattr(settings, 'ADMIN_NOTICE_TEXT', 'PROD'),
        'ADMIN_NOTICE_COLOR': getattr(settings, 'ADMIN_NOTICE_COLOR', 'red'),
        'ADMIN_NOTICE_COLOR_TEXT': getattr(settings, 'ADMIN_NOTICE_COLOR_TEXT', 'white'),
        'ADMIN_NOTICE_RIBBON': getattr(settings, 'ADMIN_NOTICE_RIBBON', False),
        'ENVIRONMENT_ADMIN_SELECTOR': getattr(
            settings, 'ENVIRONMENT_ADMIN_SELECTOR', 'body'),

    }
