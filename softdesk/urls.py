from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projectmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.RegisterView.as_view(), name='sign_up'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('projects/', views.ProjectListView.as_view(), name='projects_createlist'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='projects_manage'),
    path('projects/<int:project_id>/users/', views.ProjectContributorListCreateView.as_view(), name='projects_users_createlist'),
    path('projects/<int:project_id>/users/<int:pk>/', views.ProjectContributorDeleteView.as_view(), name='projects_users_delete'),
]
