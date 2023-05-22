# Generated by Django 4.2 on 2023-04-28 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cartao', models.CharField(max_length=20)),
                ('cvv', models.IntegerField()),
                ('data_vencimento', models.DateField()),
                ('bandeira', models.CharField(max_length=20)),
                ('nome_titular_cartao', models.CharField(max_length=100)),
                ('cartao_ativo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Cartao',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='foto_perfil')),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('data_nascimento_criacao', models.DateField()),
                ('usuario', models.CharField(max_length=20)),
                ('senha', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_conta', models.CharField(choices=[('CC', 'Conta Corrente'), ('CS', 'Conta Salário'), ('CP', 'Conta Poupança')], default='CC', max_length=2)),
                ('numero_conta', models.IntegerField()),
                ('agencia', models.IntegerField()),
                ('digito', models.IntegerField()),
                ('saldo', models.IntegerField()),
                ('data_criacao', models.DateField(auto_now=True)),
                ('conta_ativa', models.BooleanField()),
                ('nome_cliente_conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.cliente')),
            ],
            options={
                'verbose_name_plural': 'Conta',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapa'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceara'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piaui'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SP', 'São Paulo'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal')], default='SP', max_length=2)),
                ('complemento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cliente', models.CharField(choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now=True)),
                ('operacao', models.CharField(choices=[('D', 'Operação de débito'), ('C', 'Operação de crédito'), ('T', 'Operação de transferência')], default='D', max_length=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo_cartao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contas.cartao')),
            ],
        ),
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aporte', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rentabilidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('finalizado', models.BooleanField()),
                ('codigo_conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateField()),
                ('valor_solicitado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('juros', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aprovado', models.BooleanField()),
                ('numero_parcela', models.IntegerField()),
                ('data_aprovacao', models.DateField()),
                ('observacao', models.TextField()),
                ('codigo_conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('observacao', models.CharField(max_length=255)),
                ('codigo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contas.cliente')),
            ],
            options={
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='ClienteConta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.cliente')),
                ('codigo_conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.conta')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contas.endereco'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.tipocliente'),
        ),
        migrations.AddField(
            model_name='cartao',
            name='conta_cartao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contas.conta'),
        ),
        migrations.AddConstraint(
            model_name='cliente',
            constraint=models.UniqueConstraint(fields=('usuario',), name='unique_cliente_user'),
        ),
        migrations.AddConstraint(
            model_name='cartao',
            constraint=models.UniqueConstraint(fields=('numero_cartao',), name='unique_numero_cartao'),
        ),
    ]