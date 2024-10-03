from django.shortcuts import get_object_or_404
from django.db import IntegrityError, transaction
from drf_spectacular.utils import extend_schema, PolymorphicProxySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from icecream import ic
from courses.serializers import CourseSerializer, CourseCreateSerializer
from courses.models import Course
from rest_framework import viewsets
from rest_framework.response import Response


class CourseViewSet(viewsets.ViewSet):
    # permission_classes = [AllowAny, ]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    @extend_schema(
        responses=PolymorphicProxySerializer(
            component_name='CourseViewSet.list.responses',
            serializers=[CourseSerializer, ],
            resource_type_field_name=None,
            many=True
        )
    )
    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    @extend_schema(
        request=PolymorphicProxySerializer(
            component_name='CourseViewSet.create.request',
            serializers=[CourseCreateSerializer, ],
            resource_type_field_name='CourseViewSet.create.request',
        ),
        responses=PolymorphicProxySerializer(
            component_name='CourseViewSet.create.responses',
            serializers=[CourseSerializer, ],
            resource_type_field_name=None,
        )
    )
    def create(self, request):
        _data = request.data
        try:
            with transaction.atomic():
                _serializer = CourseCreateSerializer(data=_data)
                if _serializer.is_valid():
                    _new_course = _serializer.save()
                    _student_serializer = CourseSerializer(_new_course)
                    return Response(
                        {
                            'detail': 'Course created successfully.',
                            'course': _student_serializer.data,
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    raise Exception(_serializer.errors)

        except IntegrityError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses=PolymorphicProxySerializer(
            component_name='CourseViewSet.retrieve.responses',
            serializers=[CourseSerializer, ],
            resource_type_field_name=None,
        )
    )
    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    @extend_schema(
        request=PolymorphicProxySerializer(
            component_name='CourseViewSet.patch.request',
            serializers=[CourseCreateSerializer, ],
            resource_type_field_name='CourseViewSet.patch.request',
        ),
        responses=PolymorphicProxySerializer(
            component_name='CourseViewSet.patch.responses',
            serializers=[CourseSerializer, ],
            resource_type_field_name=None,
        )
    )
    def partial_update(self, request, pk=None):
        _data = request.data
        try:
            with transaction.atomic():
                queryset = Course.objects.all()
                course = get_object_or_404(queryset, pk=pk)
                _serializer = CourseCreateSerializer(instance=course, data=_data, partial=True)
                if _serializer.is_valid():
                    _course = _serializer.save()
                    _course_serializer = CourseSerializer(_course)
                    return Response(
                        {
                            'detail': 'Course partial update completed successfully.',
                            'course': _course_serializer.data,
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    raise Exception(_serializer.errors)

        except IntegrityError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            _course = Course.objects.get(pk=pk)
            _course.students.clear()
            _course.delete()
            return Response(
                {
                    'detail': 'Course deleted successfully.',
                },
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            ic(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
