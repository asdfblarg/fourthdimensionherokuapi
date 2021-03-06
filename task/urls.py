from django.conf.urls import url, include
from task import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
# router.register(r'derp', views.DerpViewSet)
router.register(r'announcements', views.AnnouncementsViewSet)
router.register(r'users', views.UsersViewSet)
router.register(r'WeekSchedule', views.WeekScheduleViewSet)
router.register(r'sharedtasks', views.SharedTasksViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^tasks/test_view\.(?P<format>[a-z0-9]+)/?$',),
]