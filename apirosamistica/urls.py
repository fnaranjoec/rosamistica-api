# create this file
# rerouting all requests that have ‘api’ in the url to the <code>apps.core.urls
from django.conf.urls import url, include
from . import views as user_views
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
                    #UserListView,

                    PersonaViewSet,
                    PropiedadViewSet,
                    PersonaPropiedadViewSet,
                    UsuarioViewSet,
                    RolViewSet,

                    RolUsuarioViewSet,
                    RolUsuarioListViewSet,

                    ClienteViewSet,

                    TipoTransaccionViewSet,

                    MensajeViewSet,
                    ParametroViewSet,
                    RecursoViewSet,
                    #Seguridad
                    AplicacionViewSet,
                    EventoOpcionViewSet,
                    FuncionViewSet,
                    ModuloViewSet,
                    OpcionViewSet,

                    PermisoOpcionViewSet,
                    PermisoOpcionListViewSet,

                    PermisoEventoOpcionViewSet,

                    FincaViewSet,
                    ClientetransrecursoViewSet,
                    ClientetransViewSet,
                    FlorViewSet,
                    FlorfincaViewSet,
                    FlorpropiedadViewSet,

                    TblflorrecursoViewSet,
                    TblflorrecursoListViewSet,

                    TblpedidocabeceraViewSet,
                    TblpedidodetalleViewSet,
                    TblpedidoestadodetalleViewSet,

                    FacturaBounchViewSet,
                    FacturaCabeceraViewSet,
                    FacturaDetalleViewSet,


                    #VISTAS
                    #ClienteCreditosViewSet,

                    #STORE PROCEDURES
                    MenuViewSet,
                    #ClienteEventosViewSet,
                    FacturaAbiertaViewSet,
                    EstadoCuentaViewSet,
                    SaldoFacturaViewSet,
                    SaldoClienteViewSet,

)

# API
#router = DefaultRouter()
router = DefaultRouter(trailing_slash = False)

#router.register('user', UserListView, base_name='user')

router.register('persona', PersonaViewSet, base_name='persona')
router.register('propiedad', PropiedadViewSet, base_name='propiedad')
router.register('personapropiedad', PersonaPropiedadViewSet, base_name='personapropiedad')
router.register('usuario', UsuarioViewSet, base_name='usuario')
router.register('rol', RolViewSet, base_name='rol')

router.register('rolusuario', RolUsuarioViewSet, base_name='rolusuario')
router.register('rolusuariolist', RolUsuarioListViewSet, base_name='rolusuario')

router.register('cliente', ClienteViewSet, base_name='cliente')
router.register('tipotransaccion', TipoTransaccionViewSet, base_name='tipotransaccion')

router.register('mensaje', MensajeViewSet, base_name='mensaje')

#**********************************************************************************************************************************************************************

router.register('parametro', ParametroViewSet, base_name='parametro')
router.register('recurso', RecursoViewSet, base_name='recurso')

#**********************************************************************************************************************************************************************

router.register('aplicacion', AplicacionViewSet, base_name='aplicacion')
router.register('eventoopcion', EventoOpcionViewSet, base_name='eventoopcion')
router.register('funcion', FuncionViewSet, base_name='funcion')
router.register('modulo', ModuloViewSet, base_name='modulo')
router.register('opcion', OpcionViewSet, base_name='opcion')

router.register('permisoopcion', PermisoOpcionViewSet, base_name='permisoopcion')
router.register('permisoopcionlist', PermisoOpcionListViewSet, base_name='permisoopcionlist')

router.register('permisoeventoopcion', PermisoEventoOpcionViewSet, base_name='permisoeventoopcion')

router.register('finca', FincaViewSet, base_name='finca')
router.register('clientetransrecurso', ClientetransrecursoViewSet, base_name='clientetransrecurso')
router.register('clientetrans', ClientetransViewSet, base_name='clientetrans')
router.register('flor', FlorViewSet, base_name='flor')
router.register('florfinca', FlorfincaViewSet, base_name='florfinca')
router.register('florpropiedad', FlorpropiedadViewSet, base_name='florpropiedad')
router.register('florrecurso', TblflorrecursoViewSet, base_name='florrecurso')
router.register('florrecursolist', TblflorrecursoListViewSet, base_name='florrecursolist')
router.register('pedidocabecera', TblpedidocabeceraViewSet, base_name='pedidocabecera')
router.register('pedidodetalle', TblpedidodetalleViewSet, base_name='pedidodetalle')
router.register('pedidoestadodetalle', TblpedidoestadodetalleViewSet, base_name='pedidoestadodetalle')

router.register('facturabounch', FacturaBounchViewSet, base_name='facturabounch')
router.register('facturacabecera', FacturaCabeceraViewSet, base_name='facturacabecera')
router.register('facturadetalle', FacturaDetalleViewSet, base_name='facturadetalle')

###################################### VISTAS #####################################
router.register('facturaabierta', FacturaAbiertaViewSet, base_name='facturaabierta')

###################################### STORE PROCEDURES #####################################
router.register('menu', MenuViewSet, base_name='menu')
#router.register('clienteeventos', ClienteEventosViewSet, base_name='clienteeventos')
router.register('estadocuenta', EstadoCuentaViewSet, base_name='estadocuenta')
router.register('saldofactura', SaldoFacturaViewSet, base_name='saldofactura')
router.register('saldocliente', SaldoClienteViewSet, base_name='saldocliente')

urlpatterns = router.urls
