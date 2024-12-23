from rest_framework import serializers
from books.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


# O código < fields = "__all" > seria o ato de, o atributo fields receber todos
# os atributos da classe Models, caso o programador queira utilizar somente um
# atributos, basta passar em forma de string, o nome deste atributo, se for utilizado
# dois atributos ou mais, deve ser passardo uma lista ou tupla de strings com os valores
# dos atributos a serem utilizados.

# O codigo "type: ignore" foi solicitado pelo compilador para eliminar o aviso de erro
# na importação do 'rest_framework'. Foram realizados testes de inicialização do servidor
# e tudo ocorreu bem, manteremos atenção neste trecho de código.
