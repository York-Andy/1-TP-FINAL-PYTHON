# Importar módulos
from pymysql import MySQLConnection
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# Crear la aplicación web
app = Flask(__name__)
CORS(app)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contabilidaddb'
db = SQLAlchemy(app)

# Modelar los datos
class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    correo_electronico = db.Column(db.String(100), unique=True)
    direccion = db.Column(db.String(255))
    nombre = db.Column(db.String(100))
    razon_social = db.Column(db.String(255))
    ruc = db.Column(db.String(11))
    telefono = db.Column(db.String(10))

# Rutas para la API

def obtener_clientes():
    clientes = Cliente.query.all()
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    datos_del_cliente = request.json
    nuevo_cliente = Cliente(
        correo_electronico=datos_del_cliente['correo_electronico'],
        direccion=datos_del_cliente['direccion'],
        nombre=datos_del_cliente['nombre'],
        razon_social=datos_del_cliente['razon_social'],
        ruc=datos_del_cliente['ruc'],
        telefono=datos_del_cliente['telefono']
    )
    db.session.add(nuevo_cliente)
    db.session.commit()
    return jsonify({'id_cliente': nuevo_cliente.id_cliente}), 201

def actualizar_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    datos_actualizados = request.json
    for key, value in datos_actualizados.items():
        setattr(cliente, key, value)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente actualizado exitosamente'}), 200

def eliminar_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente eliminado exitosamente'}), 200

# Iniciar la aplicación web
if __name__ == '__main__':
    app.run(debug=True)




