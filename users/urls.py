from django.urls import path
from users.views import (
    StudentViewSet,
    TeacherViewSet
)

urlpatterns = [
    path('students/', StudentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('students/<int:pk>/', StudentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('teachers/', TeacherViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('teachers/<int:pk>/', TeacherViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
