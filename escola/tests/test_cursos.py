from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.create(codigo='TDD',descricao='Descricao teste', nivel='A')
        self.curso_01 = Curso.objects.create(codigo='TDA',descricao='Descricao teste', nivel='I')
    
    
    def test_requisicao_para_listar_cursos(self):
        """
        Teste de requisição GET para listar cursos
        """
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_para_listar_um_curso(self):
        """
        Teste de requisiçãp GET para listar um curso
        """
        
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)
    
    def test_requisicao_para_postar_um_curso(self):
        """
        Teste de requisição POST para criar cursos
        """
        
        dados = {
            'codigo':'POO',
            'descricao':'Curso POO',
            'nivel':'A'
        }
        
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_para_editar_um_curso(self):
        """
        Teste de requisição PUT para editar um curso
        """
        dados = {
            'codigo':'POO',
            'descricao':'Curso POO',
            'nivel':'I'
        }
        
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_para_excluir_um_curso(self):
        """
        Teste de requisição DELETE para excluir um curso
        """
        
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        