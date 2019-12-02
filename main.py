import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os, time, datetime, zipfile



class Compresor:
    def __init__(self):
        #Iniciamos la libreria Gtk
        b = Gtk.Builder()
        b.add_from_file('ventana.glade')
        #Cargamos los widgets con eventos asociados
        self.venprincipal = b.get_object('venPrincipal')
        self.btnabrir = b.get_object('btnAbrir')
        self.btnsalir = b.get_object('btnSalir')
        self.btnsalirdia = b.get_object('btnSalirDia')
        self.vendialogo = b.get_object('venDialogo')
        self.btncomprimir = b.get_object('btnComprimir')
        self.lblruta = b.get_object('lblRuta')
        self.lblmensaje = b.get_object('lblMensaje')

        #Diccionario eventos
        dic = {'on_venPrincipal_destroy': self.salir, 'on_btnAbrir_clicked': self.abrirdia,
               'on_btnSalir_clicked': self.salir, 'on_venDialogo_destroy': self.cerrardia, 'on_btnComprimir_clicked': self.comprimir,
               'on_venDialogo_selection_changed': self.selfile, 'on_btnSalirDia_clicked': self.cerrardia,
               }

        #conectamos y mostramos
        b.connect_signals(dic)
        self.venprincipal.show()

    def salir(self, widget):
        Gtk.main_quit()

    def abrirdia(self, widget):
        self.vendialogo.show()
        self.lblmensaje.set_text("")

    def cerrardia(self, widget):
        self.btnsalirdia.connect('delete-event', lambda w, e: w.hide() or True)

    def selfile(self, widget):
        try:
            #este coge toda la ruta
            self.fichero =os.path.abspath(str(self.vendialogo.get_filename()))
            #self.fichero = os.path.basename(str(self.vendialogo.get_filename()))  para coger solo el fichero
            self.lblruta.set_text("Fichero: " + self.fichero)
            if self.fichero == str(None):
                self.lblruta.set_text("Elija un fichero")
        except:
            self.lblruta.set_text("Error cerrando aplicación")
            time.sleep(3)
            Gtk.main_quit()

    def comprimir(self, widget):
        try:
            if self.fichero == str(None):
                self.lblruta.set_text("Falta fichero para comprimir")
            else:
                #El fichero zipeado contendra su nombre y el día en que se crea
                fecha = datetime.datetime.now()
                fichzip = zipfile.ZipFile(str(fecha) + "_copia.zip", "w")
                fichzip.write(self.fichero, os.path.basename(self.fichero), zipfile.ZIP_DEFLATED)
                self.lblmensaje.set_text("Fichero comprimido correctamente")
                self.vendialogo.hide()
        except:
            self.lblruta.set_text("Error compresion")
            time.sleep(3)
            Gtk.main_quit()

if __name__ == '__main__':
    main = Compresor()
    Gtk.main()
