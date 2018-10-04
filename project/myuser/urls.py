from django.conf.urls import url
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView)
from django.urls import reverse_lazy

from . import forms
from . import views


urlpatterns = [

    url(r'^login/$',
        LoginView.as_view(),
        {'authentication_form': forms.HAWCAuthenticationForm},
        'login'),
    url(r'^logout/$',
        LogoutView.as_view(),
        {'next_page': '/'},
        name='logout'),

    url(r'^new/$',
        views.create_account,
        name='new'),

    url(r'^profile/$',
        views.ProfileDetail.as_view(),
        name='settings'),
    url(r'^profile/update/$',
        views.ProfileUpdate.as_view(),
        name='profile_update'),
    url(r'^accept-new-license/$',
        views.AcceptNewLicense.as_view(),
        name='accept-new-license'),

    url(r'^password-change/$',
        views.PasswordChange.as_view(),
        name='change_password'),
    url(r'^password-reset/$', PasswordResetView.as_view(),
        {"post_reset_redirect": reverse_lazy("user:reset_password_sent"),
         "password_reset_form": forms.HAWCPasswordResetForm},
        name='reset_password'),
    url(r'^password-reset/sent/$',
        views.PasswordResetSent.as_view(),
        name='reset_password_sent'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(),
        {
            "set_password_form": forms.HAWCSetPasswordForm,
            "post_reset_redirect": reverse_lazy("user:password_reset_complete")
        },
        name='reset_password_confirm'),
    url(r'^password-reset-done/$',
        PasswordResetDoneView.as_view(),
        name='reset_password_done'),
    url(r'^password-reset/complete/$',
        views.PasswordResetSent.as_view(),
        name='reset_password_sent'),
    url(r'^password/changed/$',
        views.PasswordChanged.as_view(),
        name='password_reset_complete'),

    url(r'^(?P<pk>\d+)/set-password/$',
        views.SetUserPassword.as_view(),
        name='set_password'),
]
