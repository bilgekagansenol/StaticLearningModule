
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from user_api.views import UserProfileViewSet , UserLoginApiView , ChangePasswordView , PasswordResetRequestView , PasswordResetConfirmView 
from promptbox_api.views import PromptBoxItemViewSet
from chatbot_api import urls
from dashboard_api import urls
from user_api.views import UploadProfilePictureView
router = DefaultRouter()
router.register('user', UserProfileViewSet, basename='user')
router.register('promptbox', PromptBoxItemViewSet , basename='promptbox')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', UserLoginApiView.as_view()),
    path('api/' , include(router.urls)),
    path('api/', include('chatbot_api.urls')),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/reset-password/', PasswordResetRequestView.as_view(), name='reset-password'),
    path('api/reset-password-confirm/', PasswordResetConfirmView.as_view(), name='reset-password-confirm'),
    path('api/', include('chatbot_api.urls')),
    path('dashboard/', include('dashboard_api.urls')),
    path('api/upload-profile-picture/', UploadProfilePictureView.as_view(),name='upload-profile-picture')
]
#for development env
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

