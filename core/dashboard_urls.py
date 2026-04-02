from django.urls import path
from django.contrib.auth.views import LogoutView
from core.dashboard_views import DashboardHomeView, DashLoginView
import core.dashboard_views as core_dash
from services.dashboard_views import ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView
from projects.dashboard_views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from team.dashboard_views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView
from news.dashboard_views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardHomeView.as_view(), name='home'),
    path('login/', DashLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/dashboard/login/'), name='logout'),

    # Settings
    path('profile/', core_dash.DashboardProfileView.as_view(), name='profile'),
    path('profile/password/', core_dash.DashboardPasswordChangeView.as_view(), name='profile_password'),

    # Statistics
    path('statistics/', core_dash.StatisticListView.as_view(), name='statistics_list'),
    path('statistics/add/', core_dash.StatisticCreateView.as_view(), name='statistics_add'),
    path('statistics/<int:pk>/edit/', core_dash.StatisticUpdateView.as_view(), name='statistics_edit'),
    path('statistics/<int:pk>/delete/', core_dash.StatisticDeleteView.as_view(), name='statistics_delete'),

    # Advantages
    path('advantages/', core_dash.AdvantageListView.as_view(), name='advantages_list'),
    path('advantages/add/', core_dash.AdvantageCreateView.as_view(), name='advantages_add'),
    path('advantages/<int:pk>/edit/', core_dash.AdvantageUpdateView.as_view(), name='advantages_edit'),
    path('advantages/<int:pk>/delete/', core_dash.AdvantageDeleteView.as_view(), name='advantages_delete'),

    # Services
    path('services/', ServiceListView.as_view(), name='services_list'),
    path('services/add/', ServiceCreateView.as_view(), name='services_add'),
    path('services/<int:pk>/edit/', ServiceUpdateView.as_view(), name='services_edit'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='services_delete'),

    # Projects
    path('projects/', ProjectListView.as_view(), name='projects_list'),
    path('projects/add/', ProjectCreateView.as_view(), name='projects_add'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='projects_edit'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='projects_delete'),

    # Team
    path('team/', TeamMemberListView.as_view(), name='team_list'),
    path('team/add/', TeamMemberCreateView.as_view(), name='team_add'),
    path('team/<int:pk>/edit/', TeamMemberUpdateView.as_view(), name='team_edit'),
    path('team/<int:pk>/delete/', TeamMemberDeleteView.as_view(), name='team_delete'),

    # News
    path('news/', ArticleListView.as_view(), name='news_list'),
    path('news/add/', ArticleCreateView.as_view(), name='news_add'),
    path('news/<int:pk>/edit/', ArticleUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', ArticleDeleteView.as_view(), name='news_delete'),
]
