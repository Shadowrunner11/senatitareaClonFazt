from model import delProduct, getProducts, insertProduct, actuProduct
from view import App
from tkinter import TclError, Tk


class Controller:
    def __init__(self):
        self.App = App(Tk())
        self.refresh_table()
        self.App.btnGuardar["command"] = self.insertar
        self.App.btnDel["command"] = self.borrar
        self.App.btnActu["command"] = self.update
        self.App.mainloop()

    def refresh_table(self):
        a = self.App.tabla
        for nombre, precio, marca, cantidad, id in getProducts():
            a.item(
                a.insert(parent="", index="end", text=nombre),
                values=[precio, marca, cantidad, id],
            )

    def insertar(self):
        a = {}
        try:
            a = self.App.info
        except TclError:
            self.App.lblAviso["text"] = "Datos no validos"
        flag = True

        def helper():
            try:
                insertProduct(**a)
                self.App.tabla.delete(*self.App.tabla.get_children())
                self.refresh_table()
                return "Insertando"
            except:
                return "Datos no validos"

        for value in a.values():
            flag = flag and len(value)
        self.App.lblAviso["text"] = helper() if flag else "Campos vacios"

    def borrar(self):
        a = self.App.tabla
        for item in a.selection():
            delProduct(int((a.item(item, "values")[-1])))
        self.App.tabla.delete(*self.App.tabla.get_children())
        self.refresh_table()

    def update(self):
        a = self.App.tabla
        actuProduct(
            int(a.item(a.selection()[0], "values")[-1]), self.App.info["precio"]
        )
        self.App.tabla.delete(*self.App.tabla.get_children())
        self.refresh_table()


if __name__ == "__main__":
    Controller()
