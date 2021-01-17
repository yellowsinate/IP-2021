from rest_framework import routers
from course_app import views as course_app_views

router = routers.DefaultRouter()
router.register(r'faculty', course_app_views.FacultyViewset)
router.register(r'user', course_app_views.UserViewset)
