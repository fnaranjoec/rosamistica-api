#Create your views here.

from .models import (
                    User,
                    Tblpersona,
                    Tblpersonapropiedad,
                    Tblusuario,
                    Tblrol,
                    Tblrolusuario,
                    Tblcliente,
                    Tblpropiedad,
                    Tbltipotrans,

                    Tblmensaje,
                    Tblparametro,
                    Tblrecurso,
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
                    Tblclientetrans,
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
                    ##SPClienteEventos,
                    SPEstadoCuenta,
                    SPSaldoFactura,
                    SPSaldoCliente,

                    )

from .serializers import (
                          TokenSerializer,

                          PersonaSerializer,
                          PropiedadSerializer,
                          PersonaPropiedadSerializer,
                          UsuarioSerializer,
                          RolSerializer,

                          RolUsuarioSerializer,
                          RolUsuarioListSerializer,

                          ClienteSerializer,
                          TipoTransaccionSerializer,

                          MensajeSerializer,
                          ParametroSerializer,
                          RecursoSerializer,
                          #Seguridad
                          AplicacionSerializer,
                          EventoOpcionSerializer,
                          FuncionSerializer,
                          ModuloSerializer,
                          OpcionSerializer,

                          PermisoOpcionSerializer,
                          PermisoOpcionListSerializer,

                          PermisoEventoOpcionSerializer,
                          ClienteTransaccionRecursoSerializer,
                          ClienteTransaccionSerializer,

                          FincaSerializer,
                          FlorSerializer,
                          FlorFincaSerializer,
                          FlorPropiedadSerializer,

                          FlorRecursoSerializer,
                          FlorRecursoListSerializer,

                          PedidoCabeceraSerializer,
                          PedidoDetalleSerializer,
                          PedidoEstadoDetalleSerializer,

                          FacturaBounchSerializer,
                          FacturaCabeceraSerializer,
                          FacturaDetalleSerializer,

                          #VISTAS
                          #ClienteCreditosSerializer,
                          FacturaSaldoSerializer,


                          #STORE PROCEDURES,
                          MenuSerializer,
                          #ClienteEventosSerializer,
                          EstadoCuentaSerializer,
                          SaldoFacturaSerializer,
                          SaldoClienteSerializer,

                          )

from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string

from django.http import HttpResponse, HttpResponseRedirect, Http404
from api_rosamistica import settings

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import generics,authentication,permissions,status,viewsets
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


import logging


class BaseView():

    def login_client(self, username="", password=""):
        # get a token from DRF
        response = self.client.post(
            reverse('create-token'),
            data=json.dumps(
                {
                    'username': username,
                    'password': password
                }
            ),
            content_type='application/json'
        )
        self.token = response.data['token']
        # set the token in the header
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token


class LoginView(generics.CreateAPIView):
    """
    POST auth/login
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(generics.CreateAPIView):
    """
    POST auth/register
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        first_name = request.data.get("first_name", "")
        last_name = request.data.get("last_name", "")
        cellphone = request.data.get("cellphone", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name, cellphone=cellphone
        )
        return Response(status=status.HTTP_201_CREATED)




class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 20
    paginate_by_param = 'page_size'
    max_paginate_by = 100


"""
class UserListView(DefaultsMixin, viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
"""



#______________________________________________________ PERSONA
class PersonaViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpersona.objects.all().order_by('capepersona')
    serializer_class    = PersonaSerializer
    def get_queryset(self):
         queryset = Tblpersona.objects.all().order_by('capepersona')

         estado = self.request.GET.get('e')

         if estado:
             queryset = queryset.filter(ccepersona = estado)

         return queryset




#______________________________________________________ PROPIEDAD
class PropiedadViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpropiedad.objects.all().order_by('cnompropiedad')
    serializer_class    = PropiedadSerializer
    def get_queryset(self):
         queryset = Tblpropiedad.objects.all().order_by('cnompropiedad')

         estado = self.request.GET.get('e')

         if estado:
             queryset = queryset.filter(ccepropiedad = estado)

         return queryset


#______________________________________________________ PERSONA PROPIEDAD
class PersonaPropiedadViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpersonapropiedad.objects.all().order_by('cidpersonapropiedad')
    serializer_class    = PersonaPropiedadSerializer
    def get_queryset(self):
        queryset = Tblpersonapropiedad.objects.all().order_by('cidpersonapropiedad')

        persona = self.request.GET.get('p')

        if persona:
            queryset = queryset.filter(cidpersona = persona)

        return queryset



#______________________________________________________ USUARIO
class UsuarioViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblusuario.objects.all().order_by('cnomusuario')
    serializer_class    = UsuarioSerializer
    def get_queryset(self):
         queryset = Tblusuario.objects.all().order_by('cnomusuario')

         estado = self.request.GET.get('e')
         username = self.request.GET.get('u')
         celular = self.request.GET.get('c')
         persona = self.request.GET.get('p')

         if estado:
             queryset = queryset.filter(cceusuario = estado)

         if username:
             queryset = queryset.filter(cnomusuario = username)

         if celular:
             queryset = queryset.filter(cnucelular = celular)

         if persona:
             queryset = queryset.filter(cidpersona = persona)

         return queryset

class UsuarioList(generics.ListAPIView): # new
    queryset = Tblusuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveAPIView): # new
    queryset = Tblusuario.objects.all()
    serializer_class = UsuarioSerializer

#______________________________________________________ ROL
class RolViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblrol.objects.all().order_by('cnomrol')
    serializer_class    = RolSerializer


    def get_queryset(self):
         queryset = Tblrol.objects.all().order_by('cnomrol')

         estado = self.request.GET.get('e')

         if estado:
             queryset = queryset.filter(ccerol = estado)

         return queryset



#______________________________________________________ ROL USUARIO
class RolUsuarioViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblrolusuario.objects.all().order_by('cidrolusuario')
    serializer_class     = RolUsuarioSerializer

    def get_queryset(self):
         serializer_class = RolUsuarioListSerializer

         queryset = Tblrolusuario.objects.all().order_by('cidrolusuario')
         estado = self.request.GET.get('e')
         rol = self.request.GET.get('r')
         usuario = self.request.GET.get('u')

         if estado:
             queryset = queryset.filter(ccerolusuario = estado)

         if rol:
             queryset = queryset.filter(cidrol = rol)

         if usuario:
             queryset = queryset.filter(cidusuario = usuario)

         return queryset


class RolUsuarioListViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblrolusuario.objects.all().order_by('cidrolusuario')
    serializer_class     = RolUsuarioListSerializer

    """
    # *** OJO NO BORRAR ***  Dependiendo del metodo HTTP seleccionamos el serializador es decir UNA VIEW CON DOS SERIALIZADORES
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RolUsuarioListSerializer

        return RolUsuarioSerializer
    """

    def get_queryset(self):

         queryset = Tblrolusuario.objects.all().order_by('cidrolusuario')
         estado = self.request.GET.get('e')
         rol = self.request.GET.get('r')
         usuario = self.request.GET.get('u')

         if estado:
             queryset = queryset.filter(ccerolusuario = estado)

         if rol:
             queryset = queryset.filter(cidrol = rol)

         if usuario:
             queryset = queryset.filter(cidusuario = usuario)

         return queryset


#______________________________________________________ CLIENTE
class ClienteViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblcliente.objects.all().order_by('cidcliente')
    serializer_class    = ClienteSerializer
    def get_queryset(self):
         queryset = Tblcliente.objects.all().order_by('cidcliente')

         estado = self.request.GET.get('e')
         rolusuario = self.request.GET.get('ru')

         if rolusuario:
             queryset = queryset.filter(cidrolusuario = rolusuario)

         if estado:
             queryset = queryset.filter(ccecliente = estado)

         return queryset



#______________________________________________________ TIPO TRANSACCION
class TipoTransaccionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tbltipotrans.objects.all().order_by('cnomtipotrans')
    serializer_class    = TipoTransaccionSerializer
    def get_queryset(self):
         queryset = Tbltipotrans.objects.all().order_by('cnomtipotrans')

         estado = self.request.GET.get('e')

         if estado:
             queryset = queryset.filter(ccetipotrans = estado)

         return queryset



#**********************************************************************************************************************************************************************


#______________________________________________________ MENSAJE
class MensajeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset            = Tblmensaje.objects.all().order_by('cdsmsjecorto')
    serializer_class     = MensajeSerializer

#______________________________________________________ PARAMETRO
class ParametroViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset            = Tblparametro.objects.all().order_by('cnomparametro')
    serializer_class    = ParametroSerializer

#______________________________________________________ RECURSO
class RecursoViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblrecurso.objects.all().order_by('cnomrecurso')
    serializer_class    = RecursoSerializer

    def get_queryset(self):
        queryset = Tblrecurso.objects.all().order_by('cnomrecurso')

        tipoRecurso = self.request.GET.get('t')
        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(ccerecurso = estado)

        if tipoRecurso:
            queryset = queryset.filter(ccitiporecurso = tipoRecurso)

        return queryset


#**********************************************************************************************************************************************************************

#______________________________________________________ APLICACION
class AplicacionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblaplicacion.objects.all().order_by('cnomapp')
    serializer_class    = AplicacionSerializer

    def get_queryset(self):
        queryset = Tblaplicacion.objects.all().order_by('cnomapp')

        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(cceapp = estado)

        return queryset


#______________________________________________________ EVENTO OPCION
class EventoOpcionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset            = Tbleventoopcion.objects.all().order_by('nidpos')
    serializer_class    = EventoOpcionSerializer

#______________________________________________________ FUNCION
class FuncionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblfuncion.objects.all().order_by('nidpos')
    serializer_class    = FuncionSerializer

    def get_queryset(self):
        queryset = Tblfuncion.objects.all().order_by('nidpos')

        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(ccefun = estado)

        return queryset



#______________________________________________________ MODULO
class ModuloViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblmodulo.objects.all().order_by('nidpos')
    serializer_class    = ModuloSerializer

    def get_queryset(self):
        queryset = Tblmodulo.objects.all().order_by('nidpos')

        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(ccemod = estado)

        return queryset


#______________________________________________________ OPCION
class OpcionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset            = Tblopcion.objects.all().order_by('nnupos')
    serializer_class    = OpcionSerializer


#______________________________________________________ PERMISO OPCION
class PermisoOpcionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpermisoopcion.objects.all().order_by('cidpermopc')
    serializer_class    = PermisoOpcionSerializer

    def get_queryset(self):
        queryset = Tblpermisoopcion.objects.all().order_by('cidpermopc')

        rol = self.request.GET.get('r')
        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(ccepermopc = estado)

        if rol:
            queryset = queryset.filter(cidrol = rol)

        return queryset

class PermisoOpcionListViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpermisoopcion.objects.all().order_by('cidpermopc')
    serializer_class    = PermisoOpcionListSerializer

    def get_queryset(self):
        queryset = Tblpermisoopcion.objects.all().order_by('cidpermopc')

        rol = self.request.GET.get('r')
        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(ccepermopc = estado)

        if rol:
            queryset = queryset.filter(cidrol = rol)

        return queryset


#______________________________________________________ PERMISO EVENTO OPCION
class PermisoEventoOpcionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset            = Tblpermisoeventoopcion.objects.all().order_by('cidpermevenopc')
    serializer_class    = PermisoEventoOpcionSerializer



#______________________________________________________ FINCA
class FincaViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblfinca.objects.all().order_by('cnomfinca')
    serializer_class    = FincaSerializer

    def get_queryset(self):
         queryset = Tblfinca.objects.all().order_by('cnomfinca')

         estado = self.request.GET.get('e')
         nombre = self.request.GET.get('n')


         if estado:
             queryset = queryset.filter(ccefinca = estado)

         if nombre:
             queryset = queryset.filter(cnomfinca__contains=nombre)

         return queryset


#______________________________________________________ CLIENTE TRANSACCION
class ClientetransViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblclientetrans.objects.all().order_by('cidclientetrans')
    serializer_class    = ClienteTransaccionSerializer

    def get_queryset(self):
         queryset = Tblclientetrans.objects.all().order_by('cidclientetrans')

         estado = self.request.GET.get('e')

         cliente = self.request.GET.get('c')

         if estado:
             queryset = queryset.filter(cceclientetrans = estado)

         if cliente:
                     queryset = queryset.filter(cidcliente = cliente)
         return queryset



#______________________________________________________ CLIENTE TRANSACCION RECURSO
class ClientetransrecursoViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblclientetransrecurso.objects.all().order_by('cidclientetransrecurso')
    serializer_class    = ClienteTransaccionRecursoSerializer

    def get_queryset(self):
         queryset = Tblclientetransrecurso.objects.all().order_by('cidclientetransrecurso')

         estado = self.request.GET.get('e')
         clientetrans = self.request.GET.get('ct')

         if estado:
             queryset = queryset.filter(cceclientetransrecurso = estado)

         if clientetrans:
             queryset = queryset.filter(cidclientetrans = clientetrans)

         return queryset

#______________________________________________________ FLOR
class FlorViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblflor.objects.all().order_by('cnomflor')
    serializer_class    = FlorSerializer

    def get_queryset(self):
         queryset = Tblflor.objects.all().order_by('cnomflor')

         estado = self.request.GET.get('e')
         if estado:
             queryset = queryset.filter(cceflor = estado)
         return queryset


#______________________________________________________ FLORFINCA
class FlorfincaViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblflorfinca.objects.all().order_by('cidflorfinca')
    serializer_class    = FlorFincaSerializer

    def get_queryset(self):
         queryset = Tblflorfinca.objects.all().order_by('cidflorfinca')

         estado = self.request.GET.get('e')
         flor = self.request.GET.get('fl')

         if estado:
             queryset = queryset.filter(cceflorfinca = estado)

         if flor:
             queryset = queryset.filter(cidflor = flor)


         return queryset


#______________________________________________________ FLOR PROPIEDAD
class FlorpropiedadViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblflorpropiedad.objects.all().order_by('cidflorpropiedad')
    serializer_class    = FlorPropiedadSerializer

    def get_queryset(self):
         queryset = Tblflorpropiedad.objects.all().order_by('cidflorpropiedad')

         return queryset

#______________________________________________________ FLOR RECURSO
class TblflorrecursoViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblflorrecurso.objects.all().order_by('cidflorrecurso')
    serializer_class    = FlorRecursoSerializer

    def get_queryset(self):
         queryset = Tblflorrecurso.objects.all().order_by('cidflorrecurso')

         estado = self.request.GET.get('e')
         if estado:
             queryset = queryset.filter(cceflorrecurso = estado)
         return queryset

class TblflorrecursoListViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblflorrecurso.objects.all().order_by('cidflorrecurso')
    serializer_class    = FlorRecursoListSerializer

    def get_queryset(self):
         queryset = Tblflorrecurso.objects.all().order_by('cidflorrecurso')

         estado = self.request.GET.get('e')
         if estado:
             queryset = queryset.filter(cceflorrecurso = estado)
         return queryset


#______________________________________________________ PEDIDO CABECERA
class TblpedidocabeceraViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpedidocabecera.objects.all().order_by('cidpedido')
    serializer_class    = PedidoCabeceraSerializer

    def get_queryset(self):
         queryset = Tblpedidocabecera.objects.all().order_by('cnumpedido')

         estado = self.request.GET.get('e')

         cliente = self.request.GET.get('c')

         id = self.request.GET.get('i')

         if estado:
             queryset = queryset.filter(ccepedido = estado)

         if cliente:
             queryset = queryset.filter(cidcliente = cliente)

         if id:
             queryset = queryset.filter(cidpedido = id)

         return queryset


#______________________________________________________ PEDIDO DETALLE
class TblpedidodetalleViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpedidodetalle.objects.all().order_by('cidpedidodet')
    serializer_class    = PedidoDetalleSerializer
    search_fields       = ('cidpedidodet', 'cidflor', 'cidpedido', 'cidfinca', 'cidpedidoestadodet', 'nnutam', 'ncanhb', 'ncanqb', 'ncantallos', 'nvrpreciounit', 'cdssolicitud')

    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function
        """
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(TblpedidodetalleViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
         queryset = Tblpedidodetalle.objects.all().order_by('cidpedidodet')



         pedido = self.request.GET.get('p')


         if pedido:
             queryset = queryset.filter(cidpedido = pedido)

         return queryset


#______________________________________________________ PEDIDO ESTADO DETALLE
class TblpedidoestadodetalleViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblpedidoestadodetalle.objects.all().order_by('cnompedidoestadodet')
    serializer_class    = PedidoEstadoDetalleSerializer

    def get_queryset(self):
         queryset = Tblpedidoestadodetalle.objects.all().order_by('cnompedidoestadodet')

         estado = self.request.GET.get('e')
         if estado:
             queryset = queryset.filter(ccepedidoestadodet = estado)
         return queryset




#______________________________________________________ FACTURA BOUNCHE
class FacturaBounchViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblfacturabounch.objects.all().order_by('cnombounch')
    serializer_class    = FacturaBounchSerializer

    def get_queryset(self):
        queryset = Tblfacturabounch.objects.all().order_by('cnombounch')

        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(ccebounch = estado)

        return queryset


#______________________________________________________ FACTURA CABECERA
class FacturaCabeceraViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblfacturacabecera.objects.all().order_by('cnumfactura')
    serializer_class    = FacturaCabeceraSerializer

    def get_queryset(self):
        queryset = Tblfacturacabecera.objects.all().order_by('cnumfactura')

        estado = self.request.GET.get('e')

        cliente = self.request.GET.get('c')

        if estado:
            queryset = queryset.filter(ccefactura = estado)

        if cliente:
            queryset = queryset.filter(cidcliente = cliente)

        return queryset


#______________________________________________________ FACTURA DETALLE
class FacturaDetalleViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Tblfacturadetalle.objects.all().order_by('nnufacturalinea')
    serializer_class    = FacturaDetalleSerializer
    search_fields       = ('nnufacturalinea','cidfactura','cidfinca','cidflor','cidbouch','cidempaque','cidtipoempaque','nnutallosbounch'
                           ,'nnubounch1','nnubounch2','nnubounch3','nnubounch4','nnubounch5','nnubounch6','nnubounch7','nnubounch8','nnubounch9'
                           ,'nnutallostotal','nvttalloprecio','nvttotalprecio','ccefacturadetalle',)

    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function
        """
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(FacturaDetalleSerializer, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = Tblfacturadetalle.objects.all().order_by('nnufacturalinea')

        factura = self.request.GET.get('f')
        estado = self.request.GET.get('e')

        if factura:
            queryset = queryset.filter(cidfactura = factura)

        if estado:
            queryset = queryset.filter(ccefacturadetalle = estado)

        return queryset

#class PermisoOpcionesViewSet(viewsets.ViewSet):
#
#    def get(self, request, idOpcion):
#        opciones = Tblpermisoopcion.objects.get(cidpermopc = idOpcion)
#        opciones_serializer= PermisoEventoOpcionSerializer(opciones)
#        return Response(opciones_serializer.data) #queryset

#class PermisoEventosViewSet(viewsets.ViewSet):
#
#    def get(self, request, idEvento):
#        eventos = Tbleventoopcion.objects.get(cideventoopc = idEvento)
#        eventos_serializer= PermisoEventoOpcionSerializer(eventos)
#        return Response(eventos_serializer.data) #queryset


#############################################  STORE PROCEDURES  #########################################
#______________________________________________________ MENU
class MenuViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = SPMenu.objects.all().order_by('cidpermevenopc')
    serializer_class    = MenuSerializer

    def get_queryset(self):
        rol = self.request.GET.get('r')
        lenguaje = self.request.GET.get('l')

        queryset = SPMenu.get_menu(rol, lenguaje)

        return queryset


#______________________________________________________ ESTADO CUENTA
class EstadoCuentaViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = SPMenu.objects.all().order_by('cidpermevenopc')
    serializer_class    = EstadoCuentaSerializer

    def get_queryset(self):
        idCliente = self.request.GET.get('c')
        fechaInicio = self.request.GET.get('f')

        queryset = SPEstadoCuenta.get_estado_cuenta(idCliente, fechaInicio)

        return queryset

#______________________________________________________ SALDO FACTURA
class SaldoFacturaViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = SPMenu.objects.all().order_by('cidpermevenopc')
    serializer_class    = SaldoFacturaSerializer

    def get_queryset(self):
        idCliente = self.request.GET.get('c')

        queryset = SPSaldoFactura.get_saldo_factura(idCliente)

        return queryset

#______________________________________________________ SALDO CLIENTE
class SaldoClienteViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = SPMenu.objects.all().order_by('cidpermevenopc')
    serializer_class    = SaldoClienteSerializer

    def get_queryset(self):
        idCliente = self.request.GET.get('c')

        queryset = SPSaldoCliente.get_saldo_cliente(idCliente)

        return queryset



#############################################  VISTAS  #########################################
#______________________________________________________ PERMISO EVENTO OPCION
class FacturaAbiertaViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Vwclientecreditos.objects.all().order_by('cnompersona')
    serializer_class    = FacturaSaldoSerializer

    def get_queryset(self):
        queryset = Vwfacturasaldo.objects.all().order_by('cidcliente', 'cnufactura')

        cliente = self.request.GET.get('c')

        if cliente:
            queryset = queryset.filter(nflsaldo__gte=0)
            queryset = queryset.filter(cidcliente = cliente)

        return queryset



"""
#############################################  VISTAS  #########################################
#______________________________________________________ PERMISO EVENTO OPCION
class ClienteCreditosViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Vwclientecreditos.objects.all().order_by('cnompersona')
    serializer_class    = ClienteCreditosSerializer

    def get_queryset(self):
        queryset = Vwclientecreditos.objects.all().order_by('cnompersona')

        estado = self.request.GET.get('e')

        if estado:
            queryset = queryset.filter(ccecliente = estado)

        return queryset


#______________________________________________________ CLIENTE EVENTOS
class ClienteEventosViewSet(DefaultsMixin, viewsets.ModelViewSet):
    #queryset            = Vwclienteeventos.objects.all()
    serializer_class    = ClienteEventosSerializer

    def get_queryset(self):
        queryset = Vwclienteeventos.objects.all()

        cliente = self.request.GET.get('c')
        eventodetalle = self.request.GET.get('ced')
        tipo = self.request.GET.get('t')

        if cliente:
            queryset = queryset.filter(cidcliente = cliente)

        if eventodetalle:
            queryset = queryset.filter(cidclienteventodet = eventodetalle)

        if tipo:
            queryset = queryset.filter(csnmultiple = tipo)



        return queryset





"""



##################################################### MAIL ################################################
class SendMailSignup(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        id = self.request.GET.get('id')
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = self.request.GET.get('t')

        if id and from_email and to_email:

            print(id)
            print(to_email)
            print(from_email)

            subject = 'Activacion de Registro YO DECIDO'
            text_content = "Hi!\nHow are you?\nHere is the link to activate your account:\nhttp://localhost:4200/validar?id=%s" %(id)
            #html_content = "<form action='http://localhost:4200/pages/validar?ID=%s'><p>Usted se ha registrado en <strong>YO DECIDO</strong>, gracias por su colaboracion.</p><br><br>Para poder validar su intencion de voto por favor presione en el boton VALIDAR MI VOTO.<br><br><br><br></form>" % id
            html_content = render_to_string('acc_active_email.html',
                                            {
                                               'id': id,
                                               'host': settings.APP_HOST,
                                            })

            #print(html_content)

            #msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            #msg.attach_alternative(html_content, "text/html")



            try:
                msg = EmailMessage(subject, html_content, from_email, [to_email])
                msg.content_subtype = "html"
                msg.send()

                #send_mail(subject, html_content, from_email, [to_email])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponse('Email sent.') #HttpResponseRedirect('Email Sent')

        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')


