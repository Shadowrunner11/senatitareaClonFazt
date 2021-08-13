from model import delProduct, getProducts, insertProduct, actuProduct
from view import App
from tkinter import Tk


class Controller:
    def __init__(self):
        self.App=App(Tk())
        self.refresh_table()
        self.App.btnGuardar["command"]=self.insertar
        self.App.btnDel["command"]=self.borrar
        self.App.btnActu["command"]=self.update
        self.App.mainloop()
    def refresh_table(self):
        a=self.App.tabla
        for nombre, precio, marca, cantidad, id in getProducts():
            a.item(a.insert(parent="", index="end", text=nombre), values=[precio, marca, cantidad, id])
    def insertar(self):
        insertProduct(**self.App.info)
        self.App.tabla.delete(*self.App.tabla.get_children())
        self.refresh_table()
    def borrar(self):
        a=self.App.tabla
        for item in a.selection():
            delProduct(int((a.item(item, "values")[-1])))
        self.App.tabla.delete(*self.App.tabla.get_children())
        self.refresh_table()
    def update(self):
        a=self.App.tabla
        actuProduct(int(a.item(a.selection()[0], "values")[-1]), self.App.info["precio"])
        self.App.tabla.delete(*self.App.tabla.get_children())
        self.refresh_table()

if __name__=="__main__":
    Controller()