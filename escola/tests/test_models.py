from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.validators import numero_celular_invalido

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('Teste falhou :(')
    
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de modelo',
            email = 'teste@teste.com',
            cpf = '58429889094',
            data_nascimento = '2023-02-02',
            numero_celular = '31 98889-8981'
        )
    
    def test_verifica_atributos_de_estudante(self):
        """
        Teste que verifica os atributos do modelo de Estudante
        """
        self.assertEqual(self.estudante.nome, 'Teste de modelo')
        self.assertEqual(self.estudante.email, 'teste@teste.com')
        self.assertEqual(self.estudante.cpf, '58429889094')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.numero_celular, '31 98889-8981')
         
    
        
class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
        codigo = 'IaC',
        descricao = 'Curso avançado de infraestrutura como código',
        nivel = 'A'
        
    )
    
    def test_verifica_atributos_de_curso(self):
        """
        Teste que verifica os atributos do modelo de Curso
        """
        self.assertEqual(self.curso.codigo, 'IaC')
        self.assertEqual(self.curso.descricao, 'Curso avançado de infraestrutura como código')
        self.assertEqual(self.curso.nivel, 'A')
        
class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email = 'testematricula@email.com',
            cpf = '58429889094',
            data_nascimento = '2023-02-02',
            numero_celular = '31 98889-8981'
        )
        
        self.curso_matricula = Curso.objects.create(
            codigo = 'Iac',
            descricao = 'Curso avançado de infraestrutura como código',
            nivel = 'A'
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante_matricula,
            curso =  self.curso_matricula,
            periodo = 'M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        """
        Teste que verifica atribulos do modelo de matricula
        """
        self.assertEqual(self.estudante_matricula.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.curso_matricula.codigo, 'Iac')
        self.assertEqual(self.matricula.periodo, 'M')