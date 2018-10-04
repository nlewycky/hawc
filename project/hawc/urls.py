from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import django.views.static

from assessment import views

urlpatterns = [

    # Portal
    url(r'^$',
        views.Home.as_view(), name='home'),
    url(r'^portal/$',
        views.AssessmentList.as_view(), name='portal'),
    url(r'^robots\.txt$',
        TemplateView.as_view(template_name='robots.txt',
                             content_type='text/plain')),
    url(r'^about/$',
        views.About.as_view(), name='about'),
    url(r'^contact/$',
        views.Contact.as_view(), name='contact'),

    # Apps
    url(r'^user/',
        include(('myuser.urls', 'myuser'), namespace='user')),
    url(r'^assessment/',
        include(('assessment.urls', 'assessment'), namespace='assessment')),
    url(r'^study/',
        include(('study.urls', 'study'), namespace='study')),
    url(r'^ani/',
        include(('animal.urls', 'animal'), namespace='animal')),
    url(r'^epi/',
        include(('epi.urls', 'epi'), namespace='epi')),
    url(r'^epi-meta/',
        include(('epimeta.urls', 'epimeta'), namespace='meta')),
    url(r'^in-vitro/',
        include(('invitro.urls', 'invitro'), namespace='invitro')),
    url(r'^bmd/',
        include(('bmd.urls', 'bmd'), namespace='bmd')),
    url(r'^lit/',
        include(('lit.urls', 'lit'), namespace='lit')),
    url(r'^summary/',
        include(('summary.urls', 'summary'), namespace='summary')),
    url(r'^rob/',
        include(('riskofbias.urls', 'riskofbias'), namespace='riskofbias')),
    url(r'^mgmt/',
        include(('mgmt.urls', 'mgmt'), namespace='mgmt')),

    # Error-pages
    url(r'^403/$',
        views.Error403.as_view(), name='403'),
    url(r'^404/$',
        views.Error404.as_view(), name='404'),
    url(r'^500/$',
        views.Error500.as_view(), name='500'),

    # Change-log
    url(r'^update-session/',
        views.UpdateSession.as_view(), name='update_session'),

    # Admin
    path('batcave/', admin.site.urls),
    url(r'^selectable/',
        include('selectable.urls')),
]

# only for DEBUG, want to use static server otherwise
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/',
            include(debug_toolbar.urls)),
        url(r'^media/(?P<path>.*)$',
            django.views.static.serve,
            {'document_root': settings.MEDIA_ROOT, }),
    ]

admin.autodiscover()
