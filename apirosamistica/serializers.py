from rest_framework.exceptions import APIException

from django.db import transaction

from .models import (
                    #CustomUser,
                    Tblpersona,
                    Tblpersonapropiedad,
                    Tblusuario,
                    Tblrol,
                    Tblrolusuario,
                    Tblpropiedad,
                    Tblmensaje,
                    Tblparametro,
                    Tblrecurso,
                    Tblcliente,
                    Tbltipotrans,
                    Tblclientetrans,
                    #Seguridad
                    Tblaplicacion,
                    Tbleventoopcion,
                    Tblfuncion,
                    Tblmodulo,
                    Tblopcion,
                    Tblpermisoeventoopcion,
                    Tblpermisoopcion,
                    Tblfinca,
                    Tblclientetransrecurso,
                    Tblflor,
                    Tblflorfinca,
                    Tblflorpropiedad,
                    Tblflorrecurso,
                    Tblpedidocabecera,
                    Tblpedidodetalle,
                    Tblpedidoestadodetalle,

                    Tblfacturabounch,
                    Tblfacturacabecera,
                    Tblfacturadetalle,

                    #VISTAS
                    #Vwclientecreditos,
                    #Vwclienteeventos,

                    Vwfacturasaldo,

                    #STORE PROCEDURES
                    SPMenu,
                    #SPClienteEventos,
                    SPEstadoCuenta,
                    SPSaldoFactura,
                    SPSaldoCliente,

)
from rest_framework import serializers

"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'cellphone', 'password',)
"""


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)



class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


#________________________________________________ PERSONA
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpersona
        fields = '__all__'

    def update(self, instance, validate_data):
         if Tblusuario.objects.filter(cidpersona =instance.cidpersona, cceusuario='A').count()>0 and validate_data.get('ccepersona', instance.ccepersona)=='X':
              raise APIException("000000014")

         instance.cnompersona = validate_data.get('cnompersona', instance.cnompersona)
         instance.capepersona = validate_data.get('capepersona', instance.capepersona)
         instance.ccepersona = validate_data.get('ccepersona', instance.ccepersona)
         instance.save()
         return instance


#________________________________________________ PROPIEDAD
class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpropiedad
        fields = '__all__'


#________________________________________________ PERSONA PROPIEDAD
class PersonaPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpersonapropiedad
        fields = '__all__'


#________________________________________________ USUARIO
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblusuario
        fields = '__all__'


#________________________________________________ ROL
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblrol
        fields = ('cidrol', 'cnomrol', 'ccerol', 'ctxurlicono')

    def update(self, instance, validate_data):
        if Tblrolusuario.objects.filter(cidrol= instance.cidrol, ccerolusuario = 'A').count() > 0  and validate_data.get('ccerol', instance.ccerol) == 'X' :
              raise APIException("000000014")
        instance.cnomrol = validate_data.get('cnomrol', instance.cnomrol)
        instance.ccerol = validate_data.get('ccerol', instance.ccerol)
        instance.ctxurlicono = validate_data.get('ctxurlicono', instance.ctxurlicono)
        instance.save()
        return instance


#________________________________________________ ROL USUARIO
class RolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblrolusuario
        fields = ('cidrolusuario', 'cidrol', 'cidusuario', 'ccerolusuario')

    #verifico que no existan clientes  o ususarios con este rol
    def update(self, instance, validate_data):
        if Tblcliente.objects.filter(cidrolusuario= instance.cidrolusuario, ccecliente = 'A').count() > 0  and validate_data.get('ccerolusuario', instance.ccerolusuario) == 'X' :
              raise APIException("000000014")

        instance.cidrol         = validate_data.get('cidrol', instance.cidrol)
        instance.cidusuario     = validate_data.get('cidusuario', instance.cidusuario)
        instance.ccerolusuario  = validate_data.get('ccerolusuario', instance.ccerolusuario)
        instance.save()
        return instance


class RolUsuarioListSerializer(serializers.ModelSerializer):
    cidrol = RolSerializer();
    cidusuario = UsuarioSerializer();
    class Meta:
        model = Tblrolusuario
        fields = ('cidrolusuario', 'cidrol', 'cidusuario', 'ccerolusuario') #, 'cidrol', 'cidusuario'



#________________________________________________ TIPO TRANSACCION
class TipoTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbltipotrans
        fields = '__all__'


#________________________________________________ CLIENTE TRANSACCION
class ClienteTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblclientetrans
        #fields = '__all__'
        fields = ('cidclientetrans', 'cidtipotrans', 'cidcliente', 'dfxtrans', 'nflvalor', 'cdstrans', 'cceclientetrans', 'cidusuario', 'cnudocumento', 'cnufactura')


#________________________________________________ CLIENTE
class ClienteSerializer(serializers.ModelSerializer):
    #transacciones = ClienteTransaccionSerializer(many=True)
    class Meta:
        model = Tblcliente
        fields = ('cidcliente','cidrolusuario','ccecliente','nflcreditocliente', 'total_creditos')


#________________________________________________ MENSAJE
class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblmensaje
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MensajeSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.query_params.get('fields'):
           fields = request.query_params.get('fields')
           if fields:
              fields = fields.split(',')
              allowed = set(fields)
              existing = set(self.fields.keys())
              for field_name in existing - allowed:
                  self.fields.pop(field_name)


#**********************************************************************************************************************************************************************


#________________________________________________ PARAMETRO
class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblparametro
        fields = '__all__'


#________________________________________________ RECURSO
class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblrecurso
        fields = '__all__'



#**********************************************************************************************************************************************************************

#________________________________________________ APLICACION
class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblaplicacion
        fields = '__all__'


#________________________________________________ EVENTO OPCION
class EventoOpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbleventoopcion
        fields = '__all__'


#________________________________________________ FUNCION
class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblfuncion
        fields = '__all__'


#________________________________________________ MODULO
class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblmodulo
        fields = '__all__'

#________________________________________________ OPCION
class OpcionSerializer(serializers.ModelSerializer):
   class Meta:
        model = Tblopcion
        fields = '__all__'



#________________________________________________ PERMISO OPCION
class PermisoOpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpermisoopcion
        fields = ('cidpermopc', 'cidrol', 'cidopc', 'ccepermopc')


class PermisoOpcionListSerializer(serializers.ModelSerializer):
    cidopc = OpcionSerializer();
    permisoevento_opcion = serializers.SerializerMethodField('_get_children')

    def _get_children(self, obj):
        serializer = PermisoEventoOpcionSerializer(obj.child_list(), many=True)
        return serializer.data

    class Meta:
        model = Tblpermisoopcion
        fields = ('cidpermopc', 'cidrol', 'cidopc', 'ccepermopc', 'permisoevento_opcion')


#________________________________________________ PERMISO EVENTO OPCION
class PermisoEventoOpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpermisoeventoopcion
        fields = ('cidpermevenopc', 'cideventoopc', 'cidpermopc', 'ccepermevenopc')

class PermisoEventoOpcionListSerializer(serializers.ModelSerializer):
    cideventoopc = EventoOpcionSerializer();
    cidpermopc =  PermisoOpcionSerializer();
    class Meta:
        model = Tblpermisoeventoopcion
        fields = ('cidpermevenopc', 'cideventoopc', 'cidpermopc', 'ccepermevenopc')


#________________________________________________ FINCA
class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblfinca
        fields = '__all__'


#________________________________________________ CLIENTE TRANSACCION RECURSO
class ClienteTransaccionRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblclientetransrecurso
        fields = ('cidclientetransrecurso', 'cidrecurso', 'cidclientetrans', 'cceclientetransrecurso')



#________________________________________________ FLOR
class FlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblflor
        fields = ('cidflor', 'cnomflor', 'cceflor')




#________________________________________________ FLOR FINCA
class FlorFincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblflorfinca
        fields = ('cidflorfinca', 'cidfinca', 'cidflor', 'cceflorfinca')



#________________________________________________ FLOR PROPIEDAD
class FlorPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblflorpropiedad
        fields = ('cidflorpropiedad', 'cidpropiedad', 'cidflor', 'ctxvalorpropiedad')



#________________________________________________ FLOR RECURSO
class FlorRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblflorrecurso
        fields = ('cidflorrecurso', 'cidflor', 'cidrecurso', 'cceflorrecurso')


class FlorRecursoListSerializer(serializers.ModelSerializer):
    cidflor=FlorSerializer()
    cidrecurso=RecursoSerializer()
    #flor_recursos=RecursoSerializer(many=True)
    class Meta:
        model = Tblflorrecurso
        fields = ('cidflorrecurso', 'cidflor', 'cidrecurso', 'cceflorrecurso') #'flor_recursos'



#________________________________________________ PEDIDO CABECERA
class PedidoCabeceraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpedidocabecera
        fields = ('cidpedido', 'cnumpedido', 'dfxpedido', 'cciestado', 'cnumprealert', 'dfxprealert', 'ccepedido', 'cidcliente')



#________________________________________________ PEDIDO DETALLE
class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpedidodetalle
        fields = ('cidpedidodet', 'cidflor', 'cidpedido', 'cidfinca', 'cidpedidoestadodet', 'nnutam', 'ncanhb', 'ncanqb', 'ncantallos', 'nvrpreciounit', 'cdssolicitud')



#________________________________________________ PEDIDO ESTADO DETALLE
class PedidoEstadoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpedidoestadodetalle
        fields = ('cidpedidoestadodet', 'cnompedidoestadodet', 'ccepedidoestadodet')


#________________________________________________ FACTURA BOUNCHES
class FacturaBounchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblfacturabounch
        fields = '__all__'

#________________________________________________ FACTURA CABECERA
class FacturaCabeceraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblfacturacabecera
        fields = '__all__'

#________________________________________________ FACTURA DETALLE
class FacturaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblfacturadetalle
        fields = '__all__'

##################################  STORE PROCEDURE  #############################################
#________________________________________________ MENU
class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPMenu
        fields = '__all__'
        #('title', 'icon', 'link', 'home',)


#________________________________________________ FACTURA SALDO
class FacturaSaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vwfacturasaldo
        fields = ('cidclientetrans','cidcliente','cnufactura','dfxtrans','nflsaldo')


#________________________________________________ ESTADO CUENTA
class EstadoCuentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPEstadoCuenta
        fields = '__all__'

#________________________________________________ SALDO FACTURA
class SaldoFacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPSaldoFactura
        fields = '__all__'


#________________________________________________ SALDO CLIENTE
class SaldoClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPSaldoCliente
        fields = '__all__'

"""

##################################  VISTAS  #############################################
#________________________________________________ CLIENTE CREDITOS
class ClienteCreditosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vwclientecreditos
        fields = '__all__'

#________________________________________________ CLIENTE CREDITOS
class ClienteEventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vwclienteeventos
        fields = '__all__'




"""




"""
#________________________________________________ CLIENTE EVENTOS
class ClienteEventosSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPClienteEventos
        fields = ('ID', 'CIdCliente', 'CNomDetalle', 'CNomEvento', 'CSNMultiple', 'NFlTotalEvento', 'DFxClienteEventoDet', 'CNomCompetidorA', 'CNomCompetidorB', 'CTxUrlIconoA', 'CTxUrlIconoB', 'CNomEventoPronostico', 'CCiCompetidor')
"""
