from django.shortcuts import get_object_or_404
from django.db import IntegrityError, transaction
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from users.serializers import StudentSerializer, TeacherSerializer, LoginViewSerializer
from users.models import Student, Teacher, User
from rest_framework import viewsets
from rest_framework.response import Response


class LoginView(TokenObtainPairView):
    serializer_class = LoginViewSerializer


class StudentViewSet(viewsets.ViewSet):
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

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        _data = request.data
        data = {
            "email": _data.get("email"),
            "user_type": _data.get("user_type"),
            "first_name": _data.get("first_name"),
            "last_name": _data.get("last_name"),
            "is_active": _data.get("is_active", False),
            "username": _data.get("email"),
            "password": _data.get("password"),
        }
        try:
            with transaction.atomic():
                if User.objects.filter(username=data.get("username")).exists():
                    return Response(
                        {"error": "Username is not unique"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                new_user = User.objects.create(**data)

                new_student = Student.objects.create(
                    user=new_user,
                    registration=_data.get("registration"),
                    name=_data.get("name"),
                )

                user_serializer = StudentSerializer(new_student)
                return Response(
                    {
                        "detail": "Student created successfully.",
                        "student": user_serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )

        except IntegrityError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


from django.shortcuts import render

# Create your views here.
