from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(nome = 'Teste Estudante Um', 
                                                     email = 'teste@estudante.com', 
                                                     cpf ='09343316003', 
                                                     data_nascimento = '2000-01-01', 
                                                     numero_celular='31 00000-0000')
        self.estudante_02 = Estudante.objects.create(nome = 'Teste Estudante Dois', 
                                                     email = 'teste02@estudante.com', 
                                                     cpf ='11052718035', 
                                                     data_nascimento = '2000-01-01', 
                                                     numero_celular='31 10000-0000')
        
    def test_requisicao_para_listar_estudantes(self):
        """
        Teste para verificar a requisição GET para listar estudantes
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_requisicao_para_listar_um_estudante(self):
        """
        Teste para verificar a requisição GET para listar um estudante
        """
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)
    
    def test_requisicao_para_criar_um_estudante(self):
        """
        Teste de requisição POST para criar um estudante
        """
        
        dados = {
            'nome' : 'Teste', 
            'email' : 'testePost@estudante.com', 
            'cpf' :'85304567005', 
            'data_nascimento' : '2000-01-01', 
            'numero_celular':'31 12000-0000'
        }
        
        response = self.client.post(self.url, data=dados)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_para_editar_um_estudante(self):
        """
        Teste de requisção PUT para editar um estudante
        """
        dados = {
            'nome' : 'TestePut', 
            'email' : 'testePut@estudante.com', 
            'cpf' :'92783904020', 
            'data_nascimento' : '2000-01-01', 
            'numero_celular':'31 12300-0000'
        }
        
        response = self.client.put(f'{self.url}1/', data=dados)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_requisicao_para_deletar_um_estudante(self):
         """
         Teste de requisição DELETE para deletar um estudante
         """
         
         response = self.client.delete(f'{self.url}2/')
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
         