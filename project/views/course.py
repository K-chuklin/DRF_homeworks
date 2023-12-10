from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from project.models import Course, Subscription
from project.permissions import IsOwnerOrStaff, IsOwner
from project.serializers.course import CourseDetailSerializer, CourseListSerializer, CourseSerializer, \
    CourseCreateSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated


class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer, *args, **kwargs):
        subscription = serializer.save()  # получаю подписку
        subscription.user = self.request.user  # сохраняю в базе юзера
        course_pk = self.kwargs.get('pk')  # сохраняю pk
        subscription.course = Course.objects.get(pk=course_pk)  # достаю нужную подписку
        subscription.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff]
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer,
        'create': CourseCreateSerializer
    }

    # Если пользователь - владелец, он может создавать курс
    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    # Фильтрация представлений по условиям
    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsOwnerOrStaff]
        elif self.action == 'create':
            permission_classes = [IsOwner]
        elif self.action == 'update':
            permission_classes = [IsOwnerOrStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

