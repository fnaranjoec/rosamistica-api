# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Cuendo quiero generar una nueva migracion
# python manage.py makemigrations --empty apirosamistica
# python manage.py migrate

from __future__ import unicode_literals
from django.conf import settings
from django.db.models import Sum
from django.db import models
from django.db import connection
from django.utils.encoding import smart_text as smart_unicode
from django.contrib.auth.models import AbstractUser




import uuid
import datetime
import django.conf as conf
import json
from decimal import Decimal


"""
from .managers import (
                      TbleventoManager,

                      )
"""


"""
class singleton:

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
"""

class User(AbstractUser):
    cellphone = models.CharField(max_length=20, blank=True)


"""
#******************************************************* djando models ********************************************************
class CustomUser(AbstractUser):
    cellphone = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.email
"""



#______________________________________ PERSONA
#@singleton
class Tblpersona(models.Model):

    cidpersona = models.CharField(db_column='CIdPersona', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnompersona = models.CharField(db_column='CNomPersona', max_length=150, blank=False, null=False)  # Field name made lowercase.
    capepersona = models.CharField(db_column='CApePersona', max_length=150, blank=False, null=False)  # Field name made lowercase.
    ccepersona = models.CharField(db_column='CCePersona', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidpersona + ' / ' + self.capepersona + ', ' + self.cnompersona)

    class Meta:
        managed = True
        db_table = 'tblpersona'
        verbose_name_plural = 'tblpersonas'
        ordering = ('capepersona','cnompersona', )


#______________________________________ PROPIEDAD
class Tblpropiedad(models.Model):
    cidpropiedad = models.CharField(db_column='CIdPropiedad', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnompropiedad = models.CharField(db_column='CNomPropiedad', unique=True, max_length=100, blank=False, null=False)  # Field name made lowercase.
    ctxetiqueta = models.CharField(db_column='CTxEtiqueta', max_length=50, blank=False, null=False)  # Field name made lowercase.
    ccitipodato = models.CharField(db_column='CCiTipoDato', max_length=1, blank=False, null=False)  # Field name made lowercase.
    nnulongitud = models.SmallIntegerField(db_column='NNuLongitud', default=0, blank=False, null=False)  # Field name made lowercase.
    ccepropiedad = models.CharField(db_column='CCePropiedad', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidpropiedad + ' / ' + self.cnompropiedad)

    class Meta:
        managed = True
        db_table = 'tblpropiedad'
        verbose_name_plural = 'tblpropiedades'
        ordering = ('cnompropiedad', )


#______________________________________ PERSONA PROPIEDAD
class Tblpersonapropiedad(models.Model):
    cidpersonapropiedad = models.CharField(db_column='CIdPersonaPropiedad', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidpropiedad = models.ForeignKey('Tblpropiedad', models.DO_NOTHING, db_column='CIdPropiedad')  # Field name made lowercase.
    cidpersona = models.ForeignKey('Tblpersona', models.DO_NOTHING, db_column='CIdPersona')  # Field name made lowercase.
    ctxvalorpropiedad = models.TextField(db_column='CTxValorPropiedad')  # Field name made lowercase.

    def __str__(self):
        return str(self.cidpersonapropiedad)

    class Meta:
        managed = True
        db_table = 'tblpersonapropiedad'
        verbose_name_plural = 'tblpersonapropiedades'
        ordering = ('cidpersonapropiedad', )



#______________________________________ USUARIO
class Tblusuario(models.Model):
    cidusuario = models.CharField(db_column='CIdUsuario', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidpersona = models.ForeignKey('Tblpersona', models.DO_NOTHING, db_column='CIdPersona')  # Field name made lowercase.
    cnomusuario = models.CharField(db_column='CNomUsuario', unique=True, max_length=50, blank=False, null=False)  # Field name made lowercase.
    ctxclave = models.CharField(db_column='CTxClave', max_length=255, blank=False, null=False)  # Field name made lowercase.
    ctxcorreo = models.CharField(db_column='CTxCorreo', unique=True, max_length=150, blank=False, null=False)  # Field name made lowercase.
    cnucelular = models.CharField(db_column='CNuCelular', unique=True, max_length=20, blank=False, null=False)  # Field name made lowercase.
    cceusuario = models.CharField(db_column='CCeUsuario', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidusuario + ' / ' + self.cnomusuario)

    class Meta:
        managed = True
        db_table = 'tblusuario'
        verbose_name_plural = 'tblusuarios'
        ordering = ('cnomusuario', )


#______________________________________ ROL
class Tblrol(models.Model):
    cidrol = models.CharField(db_column='CIdRol', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnomrol = models.CharField(db_column='CNomRol', unique=True, max_length=100)  # Field name made lowercase.
    ccerol = models.CharField(db_column='CCeRol', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.
    ctxurlicono = models.CharField(db_column='CTxUrlIcono', max_length=500, default='', blank=False, null=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidrol + ' / ' + self.cnomrol)

    class Meta:
        managed = True
        db_table = 'tblrol'
        verbose_name_plural = 'roles'
        ordering = ('cnomrol', )


#______________________________________ ROL USUARIO
class Tblrolusuario(models.Model):
    cidrolusuario = models.CharField(db_column='CIdRolUsuario', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidrol = models.ForeignKey('Tblrol', models.DO_NOTHING, db_column='cidrol', default='', related_name='rol')  # Field name made lowercase.CIdRol
    cidusuario = models.ForeignKey('Tblusuario', models.DO_NOTHING, db_column='CIdUsuario', default='', related_name='rol_usuario')  # Field name made lowercase.
    ccerolusuario = models.CharField(db_column='CCeRolUsuario', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidrolusuario + ',' + self.cidrolusuario)

    class Meta:
        managed = True
        db_table = 'tblrolusuario'
        verbose_name_plural = 'tblrolusuarios'
        ordering = ('cidrolusuario', )


#______________________________________ TIPO TRANSACCION
class Tbltipotrans(models.Model):
    cidtipotrans = models.CharField(db_column='CIdTipoTrans', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnomtipotrans = models.CharField(db_column='CNomTipoTrans', unique=True, max_length=50)  # Field name made lowercase.
    ccetipotrans = models.CharField(db_column='CCeTipoTrans', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.
    cciorigen = models.CharField(db_column='CCiOrigen', max_length=1, default='D', blank=False, null=False)  # Field name made lowercase.
    csnprincipal = models.CharField(db_column='CSNPrincipal', max_length=1, default='N', blank=False, null=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidtipotrans + ' / ' + self.cnomtipotrans)

    class Meta:
        managed = True
        db_table = 'tbltipotrans'
        verbose_name_plural = 'tbltipotransacciones'
        ordering = ('cnomtipotrans', )



#______________________________________ CLIENTE
class Tblcliente(models.Model):
    cidcliente = models.CharField(db_column='CIdCliente', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidrolusuario = models.ForeignKey('Tblrolusuario', models.DO_NOTHING, db_column='CIdRolUsuario')  # Field name made lowercase.
    ccecliente = models.CharField(db_column='CCeCliente', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.
    nflcreditocliente = models.FloatField(db_column='NFlCreditoCliente', default=0, blank=False, null=False)  # Field name made lowercase.

    @property
    def total_creditos(self):
        qs = Tblclientetrans.objects.values('cidcliente').anotate(total_creditos=Sum('nflvalor'))
        return qs['total_creditos']

    def __str__(self):
        return str(self.cidcliente)

    class Meta:
        managed = True
        db_table = 'tblcliente'
        verbose_name_plural = 'tblclientes'
        ordering = ('cidcliente', )



#______________________________________ CLIENTE TRANSACCION
class Tblclientetrans(models.Model):
    cidclientetrans = models.CharField(db_column='CIdClienteTrans', primary_key=True, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidtipotrans = models.ForeignKey('Tbltipotrans', models.DO_NOTHING, db_column='CIdTipoTrans')  # Field name made lowercase.
    cidcliente = models.ForeignKey('Tblcliente', models.DO_NOTHING, db_column='CIdCliente')  # Field name made lowercase.
    dfxtrans = models.DateTimeField(db_column='DFxTrans')  # Field name made lowercase.
    nflvalor = models.FloatField(db_column='NFlValor')  # Field name made lowercase.
    cdstrans = models.CharField(db_column='CDsTrans', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cceclientetrans = models.CharField(db_column='CCeClienteTrans', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.
    cidusuario = models.ForeignKey('Tblusuario', models.DO_NOTHING, db_column='CIdUsuario', default='')  # Field name made lowercase.
    cnudocumento = models.CharField(db_column='CNuDocumento', max_length=20, default='', blank=False, null=False)  # Field name made lowercase.
    cnufactura = models.CharField(db_column='CNuFactura', max_length=20, blank=False, null=True)  # Field name made lowercase.


    def __str__(self):
        return str(self.cidclientetrans)

    class Meta:
        managed = True
        db_table = 'tblclientetrans'
        verbose_name_plural = 'tblclientetransacciones'
        ordering = ('cidclientetrans', )



#______________________________________ MENSAJE
class Tblmensaje(models.Model):
    cidmensaje = models.CharField(db_column='CIdMensaje', primary_key=True, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cdstipoalerta = models.CharField(db_column='CDsTipoAlerta', default='success', max_length=20, blank=False, null=False)  # Field name made lowercase.
    nnuduracion = models.SmallIntegerField(db_column='NNuDuracion', default=3, blank=False, null=False)  # Field name made lowercase.
    cdstitle_en = models.CharField(db_column='CDsTitle_en', default='', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cdstitle_es = models.CharField(db_column='CDsTitle_es', default='', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cdstitle_ru = models.CharField(db_column='CDsTitle_ru', default='', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cdstitle_zh = models.CharField(db_column='CDsTitle_zh', default='', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cdsmsje_en = models.CharField(db_column='CDsMsje_en', default='', max_length=500, blank=False, null=False)  # Field name made lowercase.
    cdsmsje_es = models.CharField(db_column='CDsMsje_es', default='', max_length=500, blank=False, null=False)  # Field name made lowercase.
    cdsmsje_ru = models.CharField(db_column='CDsMsje_ru', default='', max_length=500, blank=False, null=False)  # Field name made lowercase.
    cdsmsje_zh = models.CharField(db_column='CDsMsje_zh', default='', max_length=500, blank=False, null=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidmensaje + ' / ' + self.cdsmsjecorto)

    class Meta:
        managed = True
        db_table = 'tblmensaje'
        verbose_name_plural = 'tblmensajes'
        ordering = ('cidmensaje', )



#**********************************************************************************************************************************************************************


#______________________________________ PARAMETRO
class Tblparametro(models.Model):
    cidparametro = models.CharField(db_column='CIdParametro', primary_key=True, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnomparametro = models.CharField(db_column='CNomParametro', unique=True, max_length=255)  # Field name made lowercase.
    ctxtexto = models.CharField(db_column='CTxTexto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nnuvalor = models.FloatField(db_column='NNuValor')  # Field name made lowercase.
    cdsvaloresposibles = models.CharField(db_column='CDsValoresPosibles', max_length=500)  # Field name made lowercase.

    def __str__(self):
        return str(self.cidparametro + ' / ' + self.cnomparametro)

    class Meta:
        managed = True
        db_table = 'tblparametro'
        verbose_name_plural = 'tblparametros'
        ordering = ('cidparametro', )


#______________________________________ RECURSO
class Tblrecurso(models.Model):
    cidrecurso = models.CharField(db_column='CIdRecurso', primary_key=True, max_length=36, blank=False, null=False)  # Field name made lowercase.
    ccitiporecurso = models.CharField(db_column='CCiTipoRecurso', max_length=3)  # Field name made lowercase.
    cnomrecurso = models.CharField(db_column='CNomRecurso', max_length=255)  # Field name made lowercase.
    ctxrutarecurso = models.CharField(db_column='CTxRutaRecurso', max_length=500)  # Field name made lowercase.
    ccerecurso = models.CharField(db_column='CCeRecurso', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblrecurso'
        verbose_name_plural = 'tblrecursos'
        ordering = ('cidrecurso', )



#**********************************************************************************************************************************************************************


#______________________________________ APLICACION
class Tblaplicacion(models.Model):
    cidapp = models.CharField(db_column='CIdApp', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnomapp = models.CharField(db_column='CNomApp', unique=True, max_length=100, blank=False, null=False)  # Field name made lowercase.
    csnocultaropcnoautr = models.CharField(db_column='CSNOcultarOpcNoAutr', max_length=1, blank=False, null=False)  # Field name made lowercase.
    csnaccesorapido = models.CharField(db_column='CSNAccesoRapido', max_length=1, blank=False, null=False)  # Field name made lowercase.
    cceapp = models.CharField(db_column='CCeApp', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblaplicacion'
        verbose_name_plural = 'tblaplicaciones'
        ordering = ('cidapp', )


#______________________________________ EVENTO OPCION
class Tbleventoopcion(models.Model):
    cideventoopc = models.CharField(db_column='CIdEventoOpc', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    ccievento = models.CharField(db_column='CCiEvento', max_length=20, blank=False, null=False)  # Field name made lowercase.
    cnomevento_en = models.CharField(db_column='CNomEvento_en', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnomevento_es = models.CharField(db_column='CNomEvento_es', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnomevento_ru = models.CharField(db_column='CNomEvento_ru', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnomevento_zh = models.CharField(db_column='CNomEvento_zh', max_length=100, blank=False, null=False)  # Field name made lowercase.
    ccisiglas = models.CharField(db_column='CCiSiglas', max_length=3, blank=False, null=False)  # Field name made lowercase.
    nidpos = models.SmallIntegerField(db_column='NIdPos', blank=False, null=False)  # Field name made lowercase.
    cceevento = models.CharField(db_column='CCeEvento', max_length=1)  # Field name made lowercase.
    cidapp = models.ForeignKey('Tblaplicacion', models.DO_NOTHING, db_column='CIdApp')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbleventoopcion'
        verbose_name_plural = 'tbleventoopciones'
        ordering = ('cideventoopc', )

#______________________________________ FUNCION
class Tblfuncion(models.Model):
    cidfun = models.CharField(db_column='CIdFun', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidapp = models.ForeignKey('Tblaplicacion', models.DO_NOTHING, db_column='CIdApp')  # Field name made lowercase.
    ccifun = models.CharField(db_column='CCiFun', max_length=3, blank=False, null=False)  # Field name made lowercase.
    cnomfun_en = models.CharField(db_column='CNomFun_en', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnomfun_es = models.CharField(db_column='CNomFun_es', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnomfun_ru = models.CharField(db_column='CNomFun_ru', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnomfun_zh = models.CharField(db_column='CNomFun_zh', max_length=100, blank=False, null=False)  # Field name made lowercase.
    nidpos = models.SmallIntegerField(db_column='NIdPos')  # Field name made lowercase.
    ccefun = models.CharField(db_column='CCeFun', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblfuncion'
        verbose_name_plural = 'tblfunciones'
        ordering = ('cidfun', )


#______________________________________ MODULO
class Tblmodulo(models.Model):
    cidmod = models.CharField(db_column='CIdMod', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidapp = models.ForeignKey('Tblaplicacion', models.DO_NOTHING, db_column='CIdApp')  # Field name made lowercase.
    cnommod_en = models.CharField(db_column='CNomMod_en', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnommod_es = models.CharField(db_column='CNomMod_es', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnommod_ru = models.CharField(db_column='CNomMod_ru', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnommod_zh = models.CharField(db_column='CNomMod_zh', max_length=100, blank=False, null=False)  # Field name made lowercase.
    ccimod = models.CharField(db_column='CCiMod', max_length=3, blank=False, null=False)  # Field name made lowercase.
    nidpos = models.SmallIntegerField(db_column='NIdPos')  # Field name made lowercase.
    ccemod = models.CharField(db_column='CCeMod', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblmodulo'
        verbose_name_plural = 'tblmodulos'
        ordering = ('cidmod', )

#______________________________________ OPCION
class Tblopcion(models.Model):
    cidopc = models.CharField(db_column='CIdOpc', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidapp = models.ForeignKey('Tblaplicacion', models.DO_NOTHING, db_column='CIdApp')  # Field name made lowercase.
    cidfun = models.ForeignKey('Tblfuncion', models.DO_NOTHING, db_column='CIdFun')  # Field name made lowercase.
    ctxmenu_en = models.CharField(db_column='CTxMenu_en', max_length=100, blank=False, null=False)  # Field name made lowercase.
    ctxmenu_es = models.CharField(db_column='CTxMenu_es', max_length=100, blank=False, null=False)  # Field name made lowercase.
    ctxmenu_ru = models.CharField(db_column='CTxMenu_ru', max_length=100, blank=False, null=False)  # Field name made lowercase.
    ctxmenu_zh = models.CharField(db_column='CTxMenu_zh', max_length=100, blank=False, null=False)  # Field name made lowercase.
    nnunivel = models.SmallIntegerField(db_column='NNuNivel')  # Field name made lowercase.
    nnupos = models.SmallIntegerField(db_column='NNuPos')  # Field name made lowercase.
    cidopcpadre = models.CharField(db_column='CIdOpcPadre', max_length=36)  # Field name made lowercase.
    csnultimonivel = models.CharField(db_column='CSNUltimoNivel', max_length=1)  # Field name made lowercase.
    csnseparador = models.CharField(db_column='CSNSeparador', max_length=1)  # Field name made lowercase.
    cciclase = models.CharField(db_column='CCiClase', max_length=1)  # Field name made lowercase.
    ctxclase = models.CharField(db_column='CTxClase', max_length=500, blank=False, null=False)  # Field name made lowercase.
    ctxargumento = models.CharField(db_column='CTxArgumento', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctxurlicono = models.CharField(db_column='CTxUrlIcono', max_length=500, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblopcion'
        verbose_name_plural = 'tblopciones'
        ordering = ('cidopc', )


#______________________________________ PERMISO OPCION
class Tblpermisoopcion(models.Model):
    cidpermopc = models.CharField(db_column='CIdPermOpc', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidrol = models.ForeignKey('Tblrol', models.DO_NOTHING, db_column='CIdRol', default='', related_name='permiso_rol')  # Field name made lowercase.
    cidopc = models.ForeignKey('Tblopcion', models.DO_NOTHING, db_column='CIdOpc', default='', related_name='permiso_opcion')  # Field name made lowercase.
    ccepermopc = models.CharField(db_column='CCePermOpc', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblpermisoopcion'
        verbose_name_plural = 'tblpermisoopciones'
        ordering = ('cidpermopc', )



#______________________________________ PERMISO EVENTO OPCION
class Tblpermisoeventoopcion(models.Model):
    cidpermevenopc = models.CharField(db_column='CIdPermEvenOpc', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cideventoopc = models.ForeignKey('Tbleventoopcion', models.DO_NOTHING, db_column='CIdEventoOpc', default='', related_name='permisoevento_evento')  # Field name made lowercase.
    cidpermopc = models.ForeignKey('Tblpermisoopcion', models.DO_NOTHING, db_column='CIdPermOpc', default='', related_name='permisoevento_opcion')  # Field name made lowercase.
    ccepermevenopc = models.CharField(db_column='CCePermEvenOpc', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblpermisoeventoopcion'
        verbose_name_plural = 'tblpermisoeventoopciones'
        ordering = ('cidpermevenopc', )



#______________________________________ FINCA
class Tblfinca(models.Model):
    cidfinca = models.CharField(db_column='CIdFinca', primary_key=True, max_length=36, default=uuid.uuid4, editable=False,blank=False, null=False )  # Field name made lowercase.
    cnomfinca = models.CharField(db_column='CNomFinca', unique=True, max_length=150, blank=False, null=False )  # Field name made lowercase.
    ctxubicacion = models.CharField(db_column='CTxUbicacion', max_length=500, blank=False, null=False )  # Field name made lowercase.
    ccefinca = models.CharField(db_column='CCeFinca', max_length=1, default='A', blank=False, null=False )  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblfinca'
        verbose_name_plural = 'tblfincas'
        ordering = ('cnomfinca', )

#______________________________________ CLIENTE TRANSACCION RECURSO
class Tblclientetransrecurso(models.Model):
    cidclientetransrecurso = models.CharField(db_column='CIdClienteTransRecurso', primary_key=True, max_length=36, default=uuid.uuid4, editable=False,blank=False, null=False )  # Field name made lowercase.
    cidrecurso = models.ForeignKey('Tblrecurso', models.DO_NOTHING, db_column='CIdRecurso', blank=False, null=False)  # Field name made lowercase.
    cidclientetrans = models.ForeignKey(Tblclientetrans, models.DO_NOTHING, db_column='CIdClienteTrans', blank=False, null=False)  # Field name made lowercase.
    cceclientetransrecurso = models.CharField(db_column='CCeClienteTransRecurso', max_length=1, default='A', blank=False, null=False )  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblclientetransrecurso'
        verbose_name_plural = 'tblclientetransrecursos'
        ordering = ('cidclientetransrecurso', )


#______________________________________ FLOR
class Tblflor(models.Model):
    cidflor = models.CharField(db_column='CIdFlor', primary_key=True, max_length=36, default=uuid.uuid4, editable=False,blank=False, null=False)  # Field name made lowercase.
    cnomflor = models.CharField(db_column='CNomFlor', unique=True, max_length=150, blank=False, null=False)  # Field name made lowercase.
    cceflor = models.CharField(db_column='CCeFlor', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblflor'
        verbose_name_plural = 'tblflores'
        ordering = ('cnomflor', )

#______________________________________ FLORFINCA
class Tblflorfinca(models.Model):
    cidflorfinca = models.CharField(db_column='CIdFlorFinca', primary_key=True, max_length=36, default=uuid.uuid4, editable=False, blank=False, null=False)  # Field name made lowercase.
    cidfinca = models.ForeignKey(Tblfinca, models.DO_NOTHING, db_column='CIdFinca', blank=False, null=True)  # Field name made lowercase.
    cidflor = models.ForeignKey(Tblflor, models.DO_NOTHING, db_column='CIdFlor', blank=False, null=True)  # Field name made lowercase.
    cceflorfinca = models.CharField(db_column='CCeFlorFinca', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblflorfinca'
        verbose_name_plural = 'tblflorfincas'
        ordering = ('cidflorfinca', )


#______________________________________ FLOR PROPIEDAD
class Tblflorpropiedad(models.Model):
    cidflorpropiedad = models.CharField(db_column='CIdFlorPropiedad', primary_key=True, max_length=36, default=uuid.uuid4, editable=False,blank=False, null=False)  # Field name made lowercase.
    cidpropiedad = models.ForeignKey('Tblpropiedad', models.DO_NOTHING, db_column='CIdPropiedad', blank=False, null=True)  # Field name made lowercase.
    cidflor = models.ForeignKey(Tblflor, models.DO_NOTHING, db_column='CIdFlor', blank=False, null=True)  # Field name made lowercase.
    ctxvalorpropiedad = models.TextField(db_column='CTxValorPropiedad', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblflorpropiedad'
        verbose_name_plural = 'tblflorpropiedades'
        ordering = ('cidflorpropiedad', )


#______________________________________ FLOR RECURSO
class Tblflorrecurso(models.Model):
    cidflorrecurso = models.CharField(db_column='CIdFlorRecurso', primary_key=True, max_length=36, default=uuid.uuid4, editable=False,blank=False, null=False)  # Field name made lowercase.
    cidflor = models.ForeignKey(Tblflor, models.DO_NOTHING, db_column='CIdFlor', blank=False, null=True )  # Field name made lowercase.
    cidrecurso = models.ForeignKey('Tblrecurso', models.DO_NOTHING, db_column='CIdRecurso', default= '', related_name='flor_recursos')  # Field name made lowercase.
    cceflorrecurso = models.CharField(db_column='CCeFlorRecurso', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblflorrecurso'
        verbose_name_plural = 'tblflorrecursos'
        ordering = ('cidflorrecurso', )



#______________________________________ PEDIDO CABECERA
class Tblpedidocabecera(models.Model):
    cidpedido = models.CharField(db_column='CIdPedido', primary_key=True, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnumpedido = models.CharField(db_column='CNumPedido', unique=True, max_length=10, blank=False, null=False)  # Field name made lowercase.
    dfxpedido = models.DateTimeField(db_column='DFxPedido', blank=False, null=False)  # Field name made lowercase.
    cciestado = models.CharField(db_column='CCiEstado', max_length=1, blank=False, null=False)  # Field name made lowercase.
    cnumprealert = models.CharField(db_column='CNumPreAlert', max_length=10, blank=False, null=False)  # Field name made lowercase.
    dfxprealert = models.DateTimeField(db_column='DFxPreAlert', blank=True, null=True)  # Field name made lowercase.
    ccepedido = models.CharField(db_column='CCePedido', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.
    cidcliente = models.ForeignKey(Tblcliente, models.DO_NOTHING, db_column='CIdCliente', blank=False, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblpedidocabecera'
        verbose_name_plural = 'tblpedidocabeceras'
        ordering = ('cnumpedido', )



#______________________________________ PEDIDO DETALLE
class Tblpedidodetalle(models.Model):
    cidpedidodet = models.CharField(db_column='CIdPedidoDet', primary_key=True, max_length=36,blank=False, null=False)  # Field name made lowercase.
    cidflor = models.ForeignKey(Tblflor, models.DO_NOTHING, db_column='CIdFlor', blank=False, null=True)  # Field name made lowercase.
    cidpedido = models.ForeignKey(Tblpedidocabecera, models.DO_NOTHING, db_column='CIdPedido', blank=False, null=True)  # Field name made lowercase.
    cidfinca = models.ForeignKey(Tblfinca, models.DO_NOTHING, db_column='CIdFinca', blank=True, null=True)  # Field name made lowercase.
    cidpedidoestadodet = models.ForeignKey('Tblpedidoestadodetalle', models.DO_NOTHING, db_column='CIdPedidoEstadoDet', blank=False, null=True)  # Field name made lowercase.
    nnutam = models.SmallIntegerField(db_column='NNuTam', blank=False, null=False)  # Field name made lowercase.
    ncanhb = models.SmallIntegerField(db_column='NCanHB', blank=False, null=False)  # Field name made lowercase.
    ncanqb = models.SmallIntegerField(db_column='NCanQB', blank=False, null=False)  # Field name made lowercase.
    ncantallos = models.IntegerField(db_column='NCanTallos', blank=False, null=False)  # Field name made lowercase.
    nvrpreciounit = models.FloatField(db_column='NVrPrecioUnit', blank=False, null=False)  # Field name made lowercase.
    cdssolicitud = models.CharField(db_column='CDsSolicitud', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblpedidodetalle'
        verbose_name_plural = 'tblpedidodetalles'
        ordering = ('cidpedidodet', )



#______________________________________ PEDIDO ESTADO DETALLE
class Tblpedidoestadodetalle(models.Model):
    cidpedidoestadodet = models.CharField(db_column='CIdPedidoEstadoDet', primary_key=True, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnompedidoestadodet = models.CharField(db_column='CNomPedidoEstadoDet', unique=True, max_length=50, blank=False, null=False)  # Field name made lowercase.
    ccepedidoestadodet = models.CharField(db_column='CCePedidoEstadoDet', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblpedidoestadodetalle'
        verbose_name_plural = 'tblpedidoestadodetalles'
        ordering = ('cnompedidoestadodet', )


#______________________________________ FACTURA BOUNCH
class Tblfacturabounch(models.Model):
    cidbouch = models.CharField(db_column='CIdBouch', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnombounch = models.CharField(db_column='CNomBounch', unique=True, max_length=255, blank=False, null=False)  # Field name made lowercase.
    ctxbounch1 = models.CharField(db_column='CTxBounch1', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch2 = models.CharField(db_column='CTxBounch2', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch3 = models.CharField(db_column='CTxBounch3', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch4 = models.CharField(db_column='CTxBounch4', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch5 = models.CharField(db_column='CTxBounch5', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch6 = models.CharField(db_column='CTxBounch6', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch7 = models.CharField(db_column='CTxBounch7', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch8 = models.CharField(db_column='CTxBounch8', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ctxbounch9 = models.CharField(db_column='CTxBounch9', max_length=20, blank=False, null=False)  # Field name made lowercase.
    ccebounch = models.CharField(db_column='CCeBounch', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblfacturabounch'
        verbose_name_plural = 'tblfacturabounches'
        ordering = ('cnombounch', )

#______________________________________ FACTURA CABECERA
class Tblfacturacabecera(models.Model):
    cidfactura = models.CharField(db_column='CIdFactura', primary_key=True, default=uuid.uuid4, editable=False, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidcliente = models.ForeignKey(Tblcliente, models.DO_NOTHING, db_column='CIdCliente')  # Field name made lowercase.
    cdsmark = models.CharField(db_column='CDsMark', max_length=100, blank=False, null=False)  # Field name made lowercase.
    cnumfactura = models.CharField(db_column='CNumFactura', unique=True, max_length=10, blank=False, null=False)  # Field name made lowercase.
    cnumpedido = models.CharField(db_column='CNumPedido', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dfxfactura = models.DateField(db_column='DFxFactura', blank=False, null=False)  # Field name made lowercase.
    ccefactura = models.CharField(db_column='CCeFactura', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.
    cdscity = models.CharField(db_column='CDsCity', max_length=50, blank=False, null=False)  # Field name made lowercase.
    ctxaddress = models.TextField(db_column='CTxAddress', blank=False, null=False)  # Field name made lowercase.
    cdsmawb = models.CharField(db_column='CDsMAWB', max_length=50, blank=False, null=False)  # Field name made lowercase.
    cdsfreightforwader = models.CharField(db_column='CDsFreightForwader', max_length=100, blank=False, null=False)  # Field name made lowercase.
    nnutotalempaques = models.IntegerField(db_column='NNuTotalEmpaques', default=0, blank=False, null=False)  # Field name made lowercase.
    nvttotalprecio = models.FloatField(db_column='NVtTotalPrecio', default=0, blank=False, null=False)  # Field name made lowercase.
    nporcdescto = models.FloatField(db_column='NPorcDescto', default=0, blank=False, null=False)  # Field name made lowercase.
    nvaldescto = models.FloatField(db_column='NValDescto', default=0, blank=False, null=False)  # Field name made lowercase.
    nvalneto = models.FloatField(db_column='NValNeto', default=0, blank=False, null=False)  # Field name made lowercase.
    nporcimpuesto = models.FloatField(db_column='NPorcImpuesto', default=0, blank=False, null=False)  # Field name made lowercase.
    nvalimpuesto = models.FloatField(db_column='NValImpuesto', default=0, blank=False, null=False)  # Field name made lowercase.
    nvalcargos = models.FloatField(db_column='NValCargos', default=0, blank=False, null=False)  # Field name made lowercase.
    ntotalfactura = models.FloatField(db_column='NTotalFactura', default=0, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblfacturacabecera'
        verbose_name_plural = 'tblfacturacabeceras'
        ordering = ('cnumfactura', )


#______________________________________ FACTURA DETALLE
class Tblfacturadetalle(models.Model):
    nnufacturalinea = models.AutoField(db_column='NNuFacturaLinea', primary_key=True)  # Field name made lowercase.
    cidfactura = models.ForeignKey(Tblfacturacabecera, models.DO_NOTHING, db_column='CIdFactura')  # Field name made lowercase.
    cidfinca = models.ForeignKey('Tblfinca', models.DO_NOTHING, db_column='CIdFinca')  # Field name made lowercase.
    cidflor = models.ForeignKey('Tblflor', models.DO_NOTHING, db_column='CIdFlor')  # Field name made lowercase.
    cidbouch = models.ForeignKey(Tblfacturabounch, models.DO_NOTHING, db_column='CIdBouch')  # Field name made lowercase.
    cidempaque = models.CharField(db_column='CIdEmpaque', max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidtipoempaque = models.CharField(db_column='CIdTipoEmpaque', max_length=36, blank=False, null=False)  # Field name made lowercase.
    nnutallosbounch = models.IntegerField(db_column='NNuTallosBounch', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch1 = models.IntegerField(db_column='NNuBounch1', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch2 = models.IntegerField(db_column='NNuBounch2', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch3 = models.IntegerField(db_column='NNuBounch3', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch4 = models.IntegerField(db_column='NNuBounch4', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch5 = models.IntegerField(db_column='NNuBounch5', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch6 = models.IntegerField(db_column='NNuBounch6', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch7 = models.IntegerField(db_column='NNuBounch7', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch8 = models.IntegerField(db_column='NNuBounch8', default=0, blank=False, null=False)  # Field name made lowercase.
    nnubounch9 = models.IntegerField(db_column='NNuBounch9', default=0, blank=False, null=False)  # Field name made lowercase.
    nnutallostotal = models.IntegerField(db_column='NNuTallosTotal', default=0, blank=False, null=False)  # Field name made lowercase.
    nvttalloprecio = models.FloatField(db_column='NVtTalloPrecio', default=0, blank=False, null=False)  # Field name made lowercase.
    nvttotalprecio = models.FloatField(db_column='NVtTotalPrecio', default=0, blank=False, null=False)  # Field name made lowercase.
    ccefacturadetalle = models.CharField(db_column='CCeFacturaDetalle', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblfacturadetalle'
        verbose_name_plural = 'tblfacturadetalles'
        ordering = ('nnufacturalinea', )


###############################  STORE PROCEDURES ###########
#________________________________________________________________________________ MENU
class SPMenu(models.Model):
    # fields
    #ID = models.CharField(max_length=10, default = '')
    CIdOpcPadre = models.CharField(max_length=36, default = '')
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    home = models.CharField(max_length=5)

    # static method to perform a fulltext search
    @staticmethod
    def get_menu(rol, lenguaje):
        conf.settings.DATABASES['default']['NAME'] = 'rosamisticadb'
        cur = connection.cursor()
        cur.execute("CALL `sps_menu`(@cidrol:={cidrol}, @ccilenguaje:={ccilenguaje});".format(cidrol=rol, ccilenguaje=lenguaje))
        results = cur.fetchall()
        cur.close()
        conf.settings.DATABASES['default']['NAME'] = 'djangodb_rosamistica'

        return [SPMenu(*row) for row in results]


#________________________________________________________________________________ ESTADO CUENTA
class SPEstadoCuenta(models.Model):

    # fields
    CIdClienteTrans = models.CharField(primary_key=True, max_length=36, default = '')
    CIdTipoTrans = models.CharField(max_length=36, default = '')
    CIdCliente = models.CharField(max_length=36, default = '')
    CIdUsuario = models.CharField(max_length=36, default = '')
    DFxTrans = models.DateTimeField(default = '')
    NFlValor = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    CDsTrans = models.CharField(max_length=500, default = '')
    CCeClienteTrans = models.CharField(max_length=1, default = '')
    CNuDocumento = models.CharField(max_length=20, default = '')
    CNuFactura = models.CharField(max_length=20, default = '')
    CNomTipoTrans = models.CharField(max_length=50, default = '')
    CNomCliente = models.CharField(max_length=255, default = '')
    NFlSaldoInicial = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    NFlDebito = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    NFlCredito = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    NFlSaldoFinal = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))

    # static method to perform a fulltext search
    @staticmethod
    def get_estado_cuenta(idCliente, fechaInicio):
        conf.settings.DATABASES['default']['NAME'] = 'rosamisticadb'
        cur = connection.cursor()
        #print("CALL `sps_cliente_estadocuenta`(@prmCIdCliente:='"+idCliente+"', @prmDFxInicio:='"+fechaInicio+"');")
        cur.execute("CALL `sps_cliente_estadocuenta`(@prmCIdCliente:='"+idCliente+"', @prmDFxInicio:='"+fechaInicio+"');")
        results = cur.fetchall()
        #results = cur.fetchone()[0]

        cur.close()
        conf.settings.DATABASES['default']['NAME'] = 'djangodb'

        return [SPEstadoCuenta(*row) for row in results]



#________________________________________________________________________________ SALDO FACTURA
class SPSaldoFactura(models.Model):

    # fields
    CIdCliente = models.CharField(max_length=36, default = '')
    CNomCliente = models.CharField(max_length=255, default = '')
    CNuFactura = models.CharField(primary_key=True, max_length=20, default = '')
    NFlDebito = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    NFlCredito = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    NFlSaldo = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    DFxTrans = models.DateTimeField(default = '')

    # static method to perform a fulltext search
    @staticmethod
    def get_saldo_factura(idCliente):
        conf.settings.DATABASES['default']['NAME'] = 'rosamisticadb'
        cur = connection.cursor()
        #print("CALL `sps_cliente_estadocuenta`(@prmCIdCliente:='"+idCliente+"', @prmDFxInicio:='"+fechaInicio+"');")
        cur.execute("CALL `sps_cliente_saldofactura`(@prmCIdCliente:='"+idCliente+"');")
        results = cur.fetchall()
        #results = cur.fetchone()[0]

        cur.close()
        conf.settings.DATABASES['default']['NAME'] = 'djangodb'

        return [SPSaldoFactura(*row) for row in results]


#________________________________________________________________________________ SALDO CLIENTE
class SPSaldoCliente(models.Model):

    # fields
    CIdCliente = models.CharField(primary_key=True, max_length=36, default = '')
    CNomCliente = models.CharField(max_length=255, default = '')
    NFlDebito = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    NFlCredito = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    NFlSaldo = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))

    # static method to perform a fulltext search
    @staticmethod
    def get_saldo_cliente(idCliente):
        conf.settings.DATABASES['default']['NAME'] = 'rosamisticadb'
        cur = connection.cursor()
        #print("CALL `sps_cliente_estadocuenta`(@prmCIdCliente:='"+idCliente+"', @prmDFxInicio:='"+fechaInicio+"');")
        cur.execute("CALL `sps_cliente_saldo`(@prmCIdCliente:='"+idCliente+"');")
        results = cur.fetchall()
        #results = cur.fetchone()[0]

        cur.close()
        conf.settings.DATABASES['default']['NAME'] = 'djangodb'

        return [SPSaldoCliente(*row) for row in results]



###################################  VISTAS ###################
#______________________________________ FACTURA SALDO
class Vwfacturasaldo(models.Model):
    cidclientetrans      = models.CharField(db_column='CIdClienteTrans', primary_key=True, max_length=36, default='', blank=False, null=False)  # Field name made lowercase.
    cidcliente      = models.CharField(db_column='CIdCliente', max_length=36, blank=False, null=False)  # Field name made lowercase.
    cnufactura      = models.CharField(db_column='CNuFactura', max_length=20, blank=False, null=False)  # Field name made lowercase.
    dfxtrans      = models.DateTimeField(db_column='DFxTrans', blank=False, null=False) # Field name made lowercase.
    nflsaldo = models.FloatField(db_column='NFlSaldo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'vwfacturasaldo'
        ordering = ('cidcliente', 'cnufactura' )


"""

###################################  VISTAS ###################
#______________________________________ PERMISO EVENTO OPCION
class Vwclientecreditos(models.Model):
    cidcliente      = models.CharField(db_column='CIdCliente', primary_key=True, max_length=36, blank=False, null=False)  # Field name made lowercase.
    cidrolusuario   = models.ForeignKey('Tblrolusuario', models.DO_NOTHING, db_column='CIdRolUsuario')  # Field name made lowercase.
    ccecliente      = models.CharField(db_column='CCeCliente', max_length=1, default='A', blank=False, null=False)  # Field name made lowercase.
    nflcreditocliente = models.FloatField(db_column='NFlCreditoCliente', default=0, blank=False, null=False)  # Field name made lowercase.
    cnompersona     = models.CharField(db_column='CNomPersona', max_length=300)  # Field name made lowercase.
    ctxcorreo       = models.CharField(db_column='CTxCorreo', max_length=150)  # Field name made lowercase.
    cnucelular      = models.CharField(db_column='CNuCelular', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'vwclientecreditos'
        ordering = ('cnompersona', )


###############################  STORE PROCEDURES ###########
"""


"""
class SPClienteEventos(models.Model):
    # fields
    #CIdClientEventoDet = models.CharField(max_length=10, default = '')
    ID = models.IntegerField(primary_key=True)
    CIdCliente = models.CharField(max_length=36)
    CNomDetalle = models.CharField(max_length=255)
    CNomEvento = models.CharField(max_length=255)
    CSNMultiple = models.CharField(max_length=1)
    NFlTotalEvento = models.FloatField()
    DFxClienteEventoDet = models.DateTimeField()
    CNomCompetidorA = models.CharField(max_length=255)
    CNomCompetidorB = models.CharField(max_length=255)
    CTxUrlIconoA = models.CharField(max_length=500)
    CTxUrlIconoB = models.CharField(max_length=500)
    CNomEventoPronostico = models.CharField(max_length=100)
    CCiCompetidor = models.CharField(max_length=1)

    # static method to perform a fulltext search
    @staticmethod
    def get_clienteeventos(cliente):
        conf.settings.DATABASES['default']['NAME'] = 'rosamisticadb'
        cur = connection.cursor()
        cur.execute("CALL `sps_clienteeventos`(@prm_cidcliente:={cidcliente});".format(cidcliente=cliente))
        results = cur.fetchall()
        cur.close()
        conf.settings.DATABASES['default']['NAME'] = 'djangodb_rosamistica'

        return [SPClienteEventos(*row) for row in results]
"""
