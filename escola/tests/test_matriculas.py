from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Matricula, Estudante, Curso
from escola.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.create(nome = 'Teste Estudante', 
                                                     email = 'teste@estudante.com', 
                                                     cpf ='09343316003', 
                                                     data_nascimento = '2000-01-01', 
                                                     numero_celular='31 00000-0000')
        self.curso = Curso.objects.create(codigo='DBT', descricao='teste descricao', nivel='A')
        self.matricula = Matricula.objects.create(estudante=self.estudante, curso=self.curso, periodo='M')
    
    
    def test_requisicao_para_listar_matriculas(self):
        """
        Teste de requisição GET para listar matriculas
        """
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_requisicao_para_criar_matriculas(self):
        """
        Teste de requisição para POST para criar matrículas
        """
        
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'M'
        }
        
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                                       
    def test_requisicao_para_editar_matriculas(self):
        """
        Teste de requisição PUT para editar matriculas 
        """
        
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.matricula.pk,
            'periodo': 'N'
        }
        
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_para_deletar_matriculas(self):
        """
        Teste de requisição DELETE para deletar matrículas
        """
        
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)