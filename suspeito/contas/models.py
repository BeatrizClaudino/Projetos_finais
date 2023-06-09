from django.db import models
from django.core.validators import MinValueValidator


class Endereco(models.Model):
    ACRE = "AC"
    ALAGOAS = "AL"
    AMAPA = "AP"
    AMAZONAS = "AM"
    BAHIA = "BA"
    CEARA = "CE"
    ESPIRITO_SANTO = "ES"
    GOIAS = "GO"
    MARANHAO = "MA"
    MATO_GROSSO = "MT"
    MATO_GROSSO_SUL = "MS"
    MINAS_GERAIS = "MG"
    PARA = "PA"
    PARANA = "PR"
    PARAIBA = "PB"
    PERNAMBUCO = "PE"
    PAIUI = "PI"
    RIO_DE_JANEIRO = "RJ"
    RIO_GRANDE_NORTE = "RN"
    RIO_GRANDE_SUL = "RS"
    RONDONIA = "RO"
    RORAIMA = "RR"
    SAO_PAULO = "SP"
    SANTA_CATARINA = "SC"
    SERGIPE = "SE"
    TOCANTINS = "TO"
    DISTRITO_FEDERAL = "DF"

    ESTADOS = [
        (ACRE, "Acre"),
        (ALAGOAS, "Alagoas"),
        (AMAPA, "Amapa"),
        (AMAZONAS, "Amazonas"),
        (BAHIA, "Bahia"),
        (CEARA, "Ceara"),
        (ESPIRITO_SANTO, "Espírito Santo"),
        (GOIAS, "Goiás"),
        (MARANHAO, "Maranhão"),
        (MATO_GROSSO, "Mato Grosso"),
        (MATO_GROSSO_SUL, "Mato Grosso do Sul"),
        (MINAS_GERAIS, "Minas Gerais"),
        (PARA, "Pará"),
        (PARANA, "Paraná"),
        (PARAIBA, "Paraíba"),
        (PERNAMBUCO, "Pernambuco"),
        (PAIUI, "Piaui"),
        (RIO_DE_JANEIRO, "Rio de Janeiro"),
        (RIO_GRANDE_NORTE, "Rio Grande do Norte"),
        (RIO_GRANDE_SUL, "Rio Grande do Sul"),
        (RONDONIA, "Rondônia"),
        (RORAIMA, "Roraima"),
        (SAO_PAULO, "São Paulo"),
        (SANTA_CATARINA, "Santa Catarina"),
        (SERGIPE, "Sergipe"),
        (TOCANTINS, "Tocantins"),
        (DISTRITO_FEDERAL, "Distrito Federal"),
    ]

    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=SAO_PAULO)
    complemento = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = "Endereço"


class TipoCliente(models.Model):
    PESSOA_FISICA = "F"
    PESSOA_JURIDICA = "J"

    TIPO_CLIENTE = [
        (PESSOA_FISICA, "Pessoa Física"),
        (PESSOA_JURIDICA, "Pessoa Jurídica"),
    ]

    tipo_cliente = models.CharField(
        max_length=1, choices=TIPO_CLIENTE, default=PESSOA_FISICA
    )


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    endereco_cliente = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="foto_perfil")
    cpf_cnpj = models.CharField(max_length=20)
    data_nascimento_criacao = models.DateField()
    usuario = models.CharField(max_length=20)
    senha = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["usuario"],
                name="unique_cliente_user",
            )
        ]
        verbose_name_plural = "Cliente"

    
class Contatos(models.Model):
    codigo_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    numero_telefone = models.IntegerField()
    email = models.EmailField()
    observacao = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Contatos"


class Conta(models.Model):
    CONTA_CORRENTE = "CC"
    CONTA_SALARIO = "CS"
    CONTA_POUPANCA = "CP"

    TIPO_CONTA = [
        (CONTA_CORRENTE, "Conta Corrente"),
        (CONTA_SALARIO, "Conta Salário"),
        (CONTA_POUPANCA, "Conta Poupança"),
    ]

    tipo_conta = models.CharField(
        max_length=2, choices=TIPO_CONTA, default=CONTA_CORRENTE
    )
    nome_cliente_conta = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    numero_conta = models.IntegerField()
    agencia = models.IntegerField()
    digito = models.IntegerField()
    saldo = models.IntegerField()
    data_criacao = models.DateField(auto_now=True)
    conta_ativa = models.BooleanField()

    class Meta:
        verbose_name_plural = "Conta"

    def __str__(self) -> str:
        return self.numero_conta


class Cartao(models.Model):
    numero_cartao = models.CharField(max_length=20)
    conta_cartao = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    cvv = models.IntegerField()
    data_vencimento = models.DateField()
    bandeira = models.CharField(max_length=20)
    nome_titular_cartao = models.CharField(max_length=100)
    cartao_ativo = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["numero_cartao"],
                name="unique_numero_cartao",
            )
        ]
        verbose_name_plural = "Cartao"


class Movimentacao(models.Model):
    DEBITO = "D"
    CREDITO = "C"
    TRANSFERENCIA = "T"

    TIPO_OPERACAO = [
        (DEBITO, "Operação de débito"),
        (CREDITO, "Operação de crédito"),
        (TRANSFERENCIA, "Operação de transferência"),
    ]

    codigo_cartao = models.ForeignKey(Cartao, on_delete=models.PROTECT)
    data_hora = models.DateTimeField(auto_now=True)
    operacao = models.CharField(max_length=1, choices=TIPO_OPERACAO, default=DEBITO)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


class Emprestimo(models.Model):
    codigo_conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    data_solicitacao = models.DateField()
    valor_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    juros = models.DecimalField(max_digits=10, decimal_places=2)
    aprovado = models.BooleanField()
    numero_parcela = models.IntegerField()
    data_aprovacao = models.DateField()
    observacao = models.TextField()


class Investimento(models.Model):
    codigo_conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    aporte = models.DecimalField(max_digits=10, decimal_places=2)
    rentabilidade = models.DecimalField(max_digits=10, decimal_places=2)
    finalizado = models.BooleanField()


class ClienteConta(models.Model):
    codigo_conta = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    codigo_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
