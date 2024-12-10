from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee,Stagiaires,Post
from .serializer import  StagiairesSerializer,EmployeSerializer,PostSerializer
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializer import EmployeSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
class StagiairesViewSet(viewsets.ModelViewSet):
    queryset = Stagiaires.objects.all().order_by('-id')  
    serializer_class = StagiairesSerializer  

    def list(self, request):
        # Récupérer tous les stagiaires
        serializer = self.get_serializer(self.queryset, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def create(self, request):
        # Créer un nouveau stagiaire
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#employe


class EmployeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains') 
    email = django_filters.CharFilter(lookup_expr='icontains') 

    class Meta:
        model = Employee
        fields = ['name', 'email']  

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['name', 'email'] 
    ordering_fields = '__all__'  
    ordering = ['id']  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            employe = serializer.save()
            subject = 'New Account Creation'
            message = (
                f'Dear {employe.name},\n\n'
                'You have been successfully registered in our employees. '
                f'Username: {employe.email}\n'
                f'Telephone: {employe.telephone}.\n\n'
                'Best regards,\nThe BTS Team.'
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[employe.email],
                fail_silently=False,
            )
            return Response({
                'message': 'Employé créé avec succès.',
                'employe': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        employe = self.get_object()  
        serializer = self.get_serializer(employe)  
        return Response(serializer.data) 





#post employee
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')  
    serializer_class = PostSerializer  

    def list(self, request):
        # Récupérer tous les posts
        serializer = self.get_serializer(self.queryset, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def create(self, request):
        # Créer un nouveau post
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid(): 
            post = serializer.save()  
            return Response({
                'message': 'Post registered successfully.',
                'post': serializer.data
            }, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

