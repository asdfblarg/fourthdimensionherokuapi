from django.conf.urls import url, include
from task import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Tasks', views.TaskViewSet)
# router.register(r'derp', views.DerpViewSet)
router.register(r'Announcements', views.AnnouncementsViewSet)
router.register(r'Users', views.UsersViewSet)
router.register(r'Week Schedule', views.WeekScheduleViewSet)
router.register(r'Shared Tasks', views.SharedTasksViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^tasks/test_view\.(?P<format>[a-z0-9]+)/?$',),
]