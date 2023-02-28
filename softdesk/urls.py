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
    path('projects/', views.ProjectListCreateView.as_view(), name='projects_createlist'),
    path('projects/<int:pk>', views.ProjectRetrieveUpdateDeleteView.as_view(), name='projects_retrieveupdatedelete'),
    path('projects/<int:project_id>/users/', views.ProjectContributorListCreateView.as_view(), name='projects_users_createlist'),
    path('projects/<int:project_id>/users/<int:pk>/', views.ProjectContributorDeleteView.as_view(), name='projects_users_delete'),
    path('projects/<int:project_id>/issues/', views.IssueListCreateView.as_view(), name='issues_createlist'),
    path('projects/<int:project_id>/issues/<int:pk>', views.IssueUpdateDeleteView.as_view(), name='issues_updatedelete'),
    path('projects/<int:project_id>/issues/<int:issue_id>/comments/', views.CommentListCreateView.as_view(), name='comments_createlist'),
    path('projects/<int:project_id>/issues/<int:issue_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDeleteView.as_view(), name='comments_retrieveupdatedelete'),
]
