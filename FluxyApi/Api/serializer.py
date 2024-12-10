from rest_framework import serializers
from .models import Employee,Stagiaires,Post

class StagiairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stagiaires
        fields = '__all__'  # Incluez tous les champs que vous souhaitez exposer

    def validate_email(self, value):
        # Vérifiez si l'email existe déjà dans la base de données
        if Stagiaires.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'surname',
            'email',
            'telephone',
            'gender',
            'salary',
            'post',
            'adress',
            'typecontrat',
            'contrat',
            'hiring_date',
            'photo',
        ] # Incluez tous les champs que vous souhaitez exposer

    def validate_email(self, value):
        # Vérifiez si l'email existe déjà dans la base de données
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['id','post_name']  # Incluez tous les champs que vous souhaitez exposer
