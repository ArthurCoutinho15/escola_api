from http.client import ImproperConnectionState
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer,EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.
    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.
    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.
    
    Metódos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    
    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    """
    queryset = Estudante.objects.all().order_by('id')
    #serializer_class = EstudanteSerializer 
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer 
    throttle_classes = [UserRateThrottle,MatriculaAnonRateThrottle]
    http_method_names = ['get','post']

class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista de Matriculas por id de Estudante
    Parâmetros:
    - pk (int): o identificador primário do objeto. Dever ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer
    
class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer