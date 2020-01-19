from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .apps.profiles import views

urlpatterns = [
    path('', include('twitterish.apps.posts.urls')),
    path('profiles', include('twitterish.apps.profiles.urls')),
    path('admin/', admin.site.urls),
    path('profile/', include('django.contrib.auth.urls')),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='auth/login.html'),
        name='login'
    ),
    path(
        'register',
        views.ProfileSignUpView.as_view(),
        name='register'
    )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
