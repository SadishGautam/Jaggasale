
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jaggasale import views
from django.contrib.auth import views as auth_views


handler404 = 'jaggasale.views.handler404'
# handler500 = 'jaggasale.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jaggasale.urls')),
    path('sites/', include('sites.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls')),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             ),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             ),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             ),
         name="password_reset_complete"),
    


    #
    # path('reset_password/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name="password_reset/password_reset.html"),
    #      name="reset_password"),
    #
    # path('reset_password_sent/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name="password_reset/password_reset_sent.html"),
    #      name="password_reset_done"),
    #
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name="password_reset/password_reset_form.html"),
    #      name="password_reset_confirm"),
    #
    # path('reset_password_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name="password_reset/password_reset_done.html"),
    #      name="password_reset_complete"),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
