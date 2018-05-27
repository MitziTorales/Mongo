from pymongo import MongoClient
from Max import Max
import Variables

idusuario=Variables.v_idusuario
nombre=Variables.v_nombre
apellido=Variables.v_apellido
sexo=Variables.v_sexo
eventoActual=Variables.v_eventoActual
estadoActual=Variables.v_estadoActual

maxdb=[
    Max(idusuario,nombre,apellido,sexo,eventoActual,estadoActual),
]

mongoClient = MongoClient('sl-us-south-1-portal.26.dblayer.com',42222)#sl-us-south-1-portal.16.dblayer.com:30271/compose ,30271


db=mongoClient.FractalA

collection=db.MaxBD

cursor = collection.find({"id_usuario":{"$in":[idusuario]}})
for fut in cursor:
    id = "%s" % (fut['id_usuario'])
    if id == idusuario:
        #print(id," iguaales")
        collection.update({"id_usuario": idusuario},{"$set": {"evento_actual": eventoActual, "estado_actual": estadoActual}})

#print(idusuario, "diferentes")
for maxdb in maxdb:
    collection.insert(maxdb.toDBCollection())

mongoClient.close()