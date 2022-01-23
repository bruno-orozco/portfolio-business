from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include


from inbox import views as inbox_views
from projects import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inbox_views.index, name="index"),

    path('analyst/', posts_views.analyst.as_view(), name="analyst"),

    path('contact-us/', posts_views.formContact.as_view(), name="contact"),
    path('thanks/', posts_views.thanks.as_view(), name="thanks"),

    path('projects/<str:title>/', posts_views.UserDetailView.as_view() , name="contact"),

    #re_path('djgango/', include('google_analytics.urls')),

] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)