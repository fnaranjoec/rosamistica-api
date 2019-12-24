# Generated by Django 2.1.2 on 2019-03-25 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apirosamistica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tblflorpropiedad',
            options={'managed': True, 'ordering': ('cidflorpropiedad',), 'verbose_name_plural': 'tblflorpropiedades'},
        ),
        migrations.AddField(
            model_name='tblclientetrans',
            name='cnudocumento',
            field=models.CharField(db_column='CNuDocumento', default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tblclientetrans',
            name='cnufactura',
            field=models.CharField(db_column='CNuFactura', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tbltipotrans',
            name='cciorigen',
            field=models.CharField(db_column='CCiOrigen', default='D', max_length=1),
        ),
        migrations.AddField(
            model_name='tbltipotrans',
            name='csnprincipal',
            field=models.CharField(db_column='CSNPrincipal', default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='tblclientetrans',
            name='cidclientetrans',
            field=models.CharField(db_column='CIdClienteTrans', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tblflorrecurso',
            name='cidrecurso',
            field=models.ForeignKey(db_column='CIdRecurso', on_delete=django.db.models.deletion.DO_NOTHING, related_name='flor_recursos', to='apirosamistica.Tblrecurso'),
        ),
        migrations.AlterField(
            model_name='tblrecurso',
            name='cidrecurso',
            field=models.CharField(db_column='CIdRecurso', max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='tblflorpropiedad',
            table='tblflorpropiedad',
        ),
    ]