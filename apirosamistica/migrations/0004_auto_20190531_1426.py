# Generated by Django 2.1.2 on 2019-05-31 19:26

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apirosamistica', '0003_auto_20190325_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tblfacturadetalle',
            fields=[
                ('nnufacturalinea', models.AutoField(db_column='NNuFacturaLinea', primary_key=True, serialize=False)),
                ('cidempaque', models.CharField(db_column='CIdEmpaque', max_length=36)),
                ('cidtipoempaque', models.CharField(db_column='CIdTipoEmpaque', max_length=36)),
                ('nnutallosbounch', models.IntegerField(db_column='NNuTallosBounch', default=0)),
                ('nnubounch1', models.IntegerField(db_column='NNuBounch1', default=0)),
                ('nnubounch2', models.IntegerField(db_column='NNuBounch2', default=0)),
                ('nnubounch3', models.IntegerField(db_column='NNuBounch3', default=0)),
                ('nnubounch4', models.IntegerField(db_column='NNuBounch4', default=0)),
                ('nnubounch5', models.IntegerField(db_column='NNuBounch5', default=0)),
                ('nnubounch6', models.IntegerField(db_column='NNuBounch6', default=0)),
                ('nnubounch7', models.IntegerField(db_column='NNuBounch7', default=0)),
                ('nnubounch8', models.IntegerField(db_column='NNuBounch8', default=0)),
                ('nnubounch9', models.IntegerField(db_column='NNuBounch9', default=0)),
                ('nnutallostotal', models.IntegerField(db_column='NNuTallosTotal', default=0)),
                ('nvttalloprecio', models.FloatField(db_column='NVtTalloPrecio', default=0)),
                ('nvttotalprecio', models.FloatField(db_column='NVtTotalPrecio', default=0)),
                ('ccefacturadetalle', models.CharField(db_column='CCeFacturaDetalle', default='A', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'tblfacturadetalles',
                'db_table': 'tblfacturadetalle',
                'ordering': ('nnufacturalinea',),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SPEstadoCuenta',
            fields=[
                ('CIdClienteTrans', models.CharField(default='', max_length=36, primary_key=True, serialize=False)),
                ('CIdTipoTrans', models.CharField(default='', max_length=36)),
                ('CIdCliente', models.CharField(default='', max_length=36)),
                ('CIdUsuario', models.CharField(default='', max_length=36)),
                ('DFxTrans', models.DateTimeField(default='')),
                ('NFlValor', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('CDsTrans', models.CharField(default='', max_length=500)),
                ('CCeClienteTrans', models.CharField(default='', max_length=1)),
                ('CNuDocumento', models.CharField(default='', max_length=20)),
                ('CNuFactura', models.CharField(default='', max_length=20)),
                ('CNomTipoTrans', models.CharField(default='', max_length=50)),
                ('CNomCliente', models.CharField(default='', max_length=255)),
                ('NFlSaldoInicial', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('NFlDebito', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('NFlCredito', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('NFlSaldoFinal', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SPSaldoCliente',
            fields=[
                ('CIdCliente', models.CharField(default='', max_length=36, primary_key=True, serialize=False)),
                ('CNomCliente', models.CharField(default='', max_length=255)),
                ('NFlDebito', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('NFlCredito', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('NFlSaldo', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SPSaldoFactura',
            fields=[
                ('CIdCliente', models.CharField(default='', max_length=36)),
                ('CNomCliente', models.CharField(default='', max_length=255)),
                ('CNuFactura', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('NFlDebito', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('NFlCredito', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('NFlSaldo', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('DFxTrans', models.DateTimeField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Tblfacturabounch',
            fields=[
                ('cidbouch', models.CharField(db_column='CIdBouch', default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('cnombounch', models.CharField(db_column='CNomBounch', max_length=255, unique=True)),
                ('ctxbounch1', models.CharField(db_column='CTxBounch1', max_length=20)),
                ('ctxbounch2', models.CharField(db_column='CTxBounch2', max_length=20)),
                ('ctxbounch3', models.CharField(db_column='CTxBounch3', max_length=20)),
                ('ctxbounch4', models.CharField(db_column='CTxBounch4', max_length=20)),
                ('ctxbounch5', models.CharField(db_column='CTxBounch5', max_length=20)),
                ('ctxbounch6', models.CharField(db_column='CTxBounch6', max_length=20)),
                ('ctxbounch7', models.CharField(db_column='CTxBounch7', max_length=20)),
                ('ctxbounch8', models.CharField(db_column='CTxBounch8', max_length=20)),
                ('ctxbounch9', models.CharField(db_column='CTxBounch9', max_length=20)),
                ('ccebounch', models.CharField(db_column='CCeBounch', default='A', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'tblfacturabounches',
                'db_table': 'tblfacturabounch',
                'ordering': ('cnombounch',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tblfacturacabecera',
            fields=[
                ('cidfactura', models.CharField(db_column='CIdFactura', default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('cdsmark', models.CharField(db_column='CDsMark', max_length=100)),
                ('cnumfactura', models.CharField(db_column='CNumFactura', max_length=10, unique=True)),
                ('cnumpedido', models.CharField(blank=True, db_column='CNumPedido', max_length=10, null=True)),
                ('dfxfactura', models.DateField(db_column='DFxFactura')),
                ('ccefactura', models.CharField(db_column='CCeFactura', default='A', max_length=1)),
                ('cdscity', models.CharField(db_column='CDsCity', max_length=50)),
                ('ctxaddress', models.TextField(db_column='CTxAddress')),
                ('cdsmawb', models.CharField(db_column='CDsMAWB', max_length=50)),
                ('cdsfreightforwader', models.CharField(db_column='CDsFreightForwader', max_length=100)),
                ('nnutotalempaques', models.IntegerField(db_column='NNuTotalEmpaques', default=0)),
                ('nvttotalprecio', models.FloatField(db_column='NVtTotalPrecio', default=0)),
                ('nporcdescto', models.FloatField(db_column='NPorcDescto', default=0)),
                ('nvaldescto', models.FloatField(db_column='NValDescto', default=0)),
                ('nvalneto', models.FloatField(db_column='NValNeto', default=0)),
                ('nporcimpuesto', models.FloatField(db_column='NPorcImpuesto', default=0)),
                ('nvalimpuesto', models.FloatField(db_column='NValImpuesto', default=0)),
                ('nvalcargos', models.FloatField(db_column='NValCargos', default=0)),
                ('ntotalfactura', models.FloatField(db_column='NTotalFactura', default=0)),
                ('cidcliente', models.ForeignKey(db_column='CIdCliente', on_delete=django.db.models.deletion.DO_NOTHING, to='apirosamistica.Tblcliente')),
            ],
            options={
                'verbose_name_plural': 'tblfacturacabeceras',
                'db_table': 'tblfacturacabecera',
                'ordering': ('cnumfactura',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vwfacturasaldo',
            fields=[
                ('cidclientetrans', models.CharField(db_column='CIdClienteTrans', default='', max_length=36, primary_key=True, serialize=False)),
                ('cidcliente', models.CharField(db_column='CIdCliente', max_length=36)),
                ('cnufactura', models.CharField(db_column='CNuFactura', max_length=20)),
                ('dfxtrans', models.DateTimeField(db_column='DFxTrans')),
                ('nflsaldo', models.FloatField(db_column='NFlSaldo')),
            ],
            options={
                'db_table': 'vwfacturasaldo',
                'ordering': ('cidcliente', 'cnufactura'),
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='tblpedidocabecera',
            name='cidpedido',
            field=models.CharField(db_column='CIdPedido', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tblpedidodetalle',
            name='cdssolicitud',
            field=models.CharField(blank=True, db_column='CDsSolicitud', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tblpedidodetalle',
            name='cidpedidodet',
            field=models.CharField(db_column='CIdPedidoDet', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tblpedidoestadodetalle',
            name='cidpedidoestadodet',
            field=models.CharField(db_column='CIdPedidoEstadoDet', max_length=36, primary_key=True, serialize=False),
        ),
    ]
