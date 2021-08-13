from tkinter import Frame, Label, Button, Entry, Tk, Variable, ttk, StringVar, LabelFrame, DoubleVar, IntVar


class App(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._info=self.datos(parent)
        cuadro=Frame(parent)
        self.tabla=ttk.Treeview(cuadro, columns=["1", "2", "3", "4"], displaycolumns=["1", "2", "3"])
        self.tabla.grid(row=0, columnspan=2)
        
        cuadro.pack()
        self.btnDel=Button(cuadro, text="Borrar")
        self.btnDel.grid(column=0, row=1, sticky="we")
        self.btnActu=Button(cuadro, text="Update")
        self.btnActu.grid(column=1, row=1, sticky="we")
    def datos(self, parent)->dict:
        lbfInfo=LabelFrame(parent, text="Informacion")
        lbfInfo.pack()
        info={
            "nombre": (producto:=StringVar()),
            "precio": (precio:=DoubleVar()),
            "marca": (marca:=StringVar()),
            "cantidad": (cantidad:=IntVar())
        }        
        self.componente(lbfInfo, "Producto", producto)
        self.componente(lbfInfo, "Precio", precio, 1)
        self.componente(lbfInfo, "Marca", marca,2)
        self.componente(lbfInfo, "Cantidad", cantidad, 3)
        self.btnGuardar=Button(lbfInfo, text="Guardar", command=lambda : print("Hola guillermo"))
        self.btnGuardar.grid(row=4, columnspan=2, sticky="we")

        return info
    def componente(self,parent, text:str, var:Variable, row=0):
        Label(parent, text=text).grid(column=0, row=row)
        Entry(parent, textvariable=var).grid(column=1, row=row)

    @property
    def info(self)->dict:
        return {key: value.get() for key, value in self._info.items()}






        

    

    

        

