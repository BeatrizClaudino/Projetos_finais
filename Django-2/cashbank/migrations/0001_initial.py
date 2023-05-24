# Generated by Django 4.2.1 on 2023-05-24 19:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=255)),
                ('celular', models.CharField(default='', max_length=20)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_nascimento', models.DateField()),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=25)),
                ('tipo', models.CharField(max_length=20)),
                ('limite', models.DecimalField(decimal_places=4, max_digits=8)),
                ('ativa', models.BooleanField(default=True)),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateField(auto_now=True)),
                ('valor', models.DecimalField(decimal_places=8, max_digits=8)),
                ('operacao', models.CharField(choices=[('PI', 'PIX'), ('DC', 'DOC')], default='PI', max_length=2)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencias_enviadas', to='cashbank.conta')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencias_recebidas', to='cashbank.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=75)),
                ('cidade', models.CharField(max_length=75)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=10)),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataSolicitacao', models.DateField(auto_now=True)),
                ('valorSolicitado', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1, message='O preço deve ser maior que 1 real'), django.core.validators.MaxValueValidator(20000)])),
                ('juros', models.FloatField()),
                ('valorComJuros', models.FloatField()),
                ('aprovado', models.BooleanField(default=False)),
                ('fk_conta_emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashbank.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cartao', models.CharField(max_length=20)),
                ('cvv', models.IntegerField()),
                ('data_vencimento', models.DateField()),
                ('bandeira', models.CharField(max_length=20)),
                ('nome_titular_cartao', models.CharField(max_length=100)),
                ('cartao_ativo', models.BooleanField(default=True)),
                ('nome_titular', models.CharField(max_length=255)),
                ('numero_conta', models.CharField(max_length=5)),
                ('fk_conta_cartao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cashbank.conta')),
            ],
            options={
                'verbose_name_plural': 'Cartao',
            },
        ),
        migrations.AddConstraint(
            model_name='cartao',
            constraint=models.UniqueConstraint(fields=('numero_cartao',), name='unique_numero_cartao'),
        ),
    ]
