from django.urls import path
from courses.views import (
    CourseViewSet
)

urlpatterns = [
    path('', CourseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', CourseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }))
]
