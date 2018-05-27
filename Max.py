class Max:

    def __init__(self, id_usuario, nombre, apellido, sexo, evento_actual, estado_actual):
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.evento_actual=evento_actual
        self.estado_actual=estado_actual

    def toDBCollection(self):
        return {

            "id_usuario":self.id_usuario,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "sexo":self.sexo,
            "evento_actual":self.evento_actual,
            "estado_actual":self.estado_actual,

        }

    def __str__(self):
        return "id_usuario : %1 - nombre %s - apellido %s - sexo %s - evento_actual %s - estado_actual %s - Color %s"\
        %(self.id_usuario,self.nombre,self.apellido,self.sexo,self.evento_actual,self.estado_actual)