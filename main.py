import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QPushButton, QTableWidgetItem
from src.configurations.DatabaseManager import DatabaseManager as SQLConnection


class MiAplicacion(QWidget):

    def __init__(self, datos):
        super().__init__()
        self.setWindowTitle("Datos de la Tabla")

        # Crear la tabla
        self.table_resultados = QTableWidget(self)

        # Configurar la tabla con los datos
        self.configurar_tabla(datos)

        # Mostrar la ventana
        self.show()

    def configurar_tabla(self, datos):
        self.table_resultados.setColumnCount(len(datos[0]))
        self.table_resultados.setRowCount(len(datos))

        for i, row in enumerate(datos):
            for j, item in enumerate(row):
                self.table_resultados.setItem(i, j, QTableWidgetItem(str(item)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = MiAplicacion()
    sys.exit(app.exec_())