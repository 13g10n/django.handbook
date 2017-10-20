from django.conf.urls import url

from authentication import views


urlpatterns = [
    url(r'^signup/$', views.Signup.as_view(), name='authentication-signup'),
    url(r'^signup/verify/$', views.SignupVerify.as_view(),
        name='authentication-signup-verify'),

    url(r'^login/$', views.Login.as_view(), name='authentication-login'),
    url(r'^logout/$', views.Logout.as_view(), name='authentication-logout'),

    url(r'^password/reset/$', views.PasswordReset.as_view(), 
        name='authentication-password-reset'),
    url(r'^password/reset/verify/$', views.PasswordResetVerify.as_view(), 
        name='authentication-password-reset-verify'),
    url(r'^password/reset/verified/$', views.PasswordResetVerified.as_view(), 
        name='authentication-password-reset-verified'),
    url(r'^password/change/$', views.PasswordChange.as_view(), 
        name='authentication-password-change'),

    url(r'^users/me/$', views.UserMe.as_view(), name='authentication-me'),
]

