from importlib import import_module
from django.test import TestCase
from yaml import serialize
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste de modelo',
            email = 'teste@teste.com',
            cpf = '58429889094',
            data_nascimento = '2023-02-02',
            numero_celular = '31 98889-8981'
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)
    
    def test_verifica_campos_serializados_de_estudante(self):
        """
        Teste que verifica os campos que estão sendo serializados de estudante
        """
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular']))
    
    def test_verifica_conteudo_dos_campos_de_estudante(self):
        """
        Teste que verifica o conteudo dos campos que estão sendo serializados de estudante
        """
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'],self.estudante.nome)
        self.assertEqual(dados['email'],self.estudante.email)
        self.assertEqual(dados['cpf'],self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'],self.estudante.data_nascimento)
        self.assertEqual(dados['numero_celular'],self.estudante.numero_celular)
        
class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo = 'IaC',
            descricao = 'Curso avançado de infraestrutura como código',
            nivel = 'A'
        ) 
        self.serializer_curso = CursoSerializer(instance= self.curso)
    
    def test_verifica_campos_serializados_de_curso(self):
        """
        Teste que verifica os campos que estão sendo serializados de curso
        """
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()), set(['id','codigo', 'descricao', 'nivel']))
        
    def test_verifica_conteudo_dos_campos_serializados_de_cursos(self):
        """
        Teste que verifica o conteúdo dos campos que estão sendo serializados de curso
        """
        dados = self.serializer_curso.data
        self.assertEqual(dados['codigo'], self.curso.codigo)
        self.assertEqual(dados['descricao'], self.curso.descricao)
        self.assertEqual(dados['nivel'], self.curso.nivel)
        
class SerializarMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante(
            nome = 'Teste de modelo',
            email = 'teste@teste.com',
            cpf = '58429889094',
            data_nascimento = '2023-02-02',
            numero_celular = '31 98889-8981'
        )
        self.curso_matricula = Curso(
            codigo = 'IaC',
            descricao = 'Curso avançado de infraestrutura como código',
            nivel = 'A'
        ) 
        
        self.matricula = Matricula(
            estudante = self.estudante_matricula,
            curso = self.curso_matricula,
            periodo = 'M'
        )
        
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)
        
    def test_verifica_campos_serializados_de_matricula(self):
        """Teste que verifica os campos que estão sendo serializados de matricula"""
        dados = self.serializer_matricula.data
        self.assertEqual(set(dados.keys()),set(['id','estudante','curso','periodo']))  
    
    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de estudante"""
        dados = self.serializer_matricula.data
        self.assertEqual(dados['estudante'],self.matricula.estudante.id)
        self.assertEqual(dados['curso'],self.matricula.curso.id)
        self.assertEqual(dados['periodo'],self.matricula.periodo)