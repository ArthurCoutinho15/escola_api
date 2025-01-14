from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']
    
    def test_carregamento_da_fixtures(self):
        """
        Teste que verifica carregamento das fixtures
        """
        
        estudante = Estudante.objects.get(cpf='18582729049')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.numero_celular, '85 96302-7527')
        self.assertEqual(curso.codigo, 'DE')