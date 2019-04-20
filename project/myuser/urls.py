from django.conf.urls import url
from django.contrib.auth.views import PasswordResetDoneView


from . import views


urlpatterns = [

    url(r'^login/$',
        views.CustomLoginView.as_view(),
        name='login'),
    url(r'^logout/$',
        views.CustomLogoutView.as_view(),
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
    url(r'^password-reset/$',
        views.CustomPasswordResetView.as_view(),
        name="reset_password"),
    url(r'^password-reset/sent/$',
        views.PasswordResetSent.as_view(),
        name='reset_password_sent'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        views.CustomPasswordResetConfirmView.as_view(),
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
