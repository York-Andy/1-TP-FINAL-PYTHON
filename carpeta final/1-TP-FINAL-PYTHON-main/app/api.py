from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask import Flask, send_from_directory



app = Flask(
    __name__
)  # Se crea una instancia de la clase Flask y se asigna a la variable app. El parámetro __name__ es una variable que representa el nombre del módulo o paquete en el que se encuentra este código. Flask utiliza este parámetro para determinar la ubicación de los recursos de la aplicación.

CORS(
    app
)  # Se utiliza el módulo CORS para habilitar el acceso cruzado entre dominios en la aplicación Flask. Esto significa que el backend permitirá solicitudes provenientes de dominios diferentes al dominio en el que se encuentra alojado el backend. Esto es útil cuando se desarrollan aplicaciones web con frontend y backend separados, ya que permite que el frontend acceda a los recursos del backend sin restricciones de seguridad del navegador. Al pasar app como argumento a CORS(), se configura CORS para aplicar las políticas de acceso cruzado a la aplicación Flask representada por app.


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:@localhost/BaseDeDatosintegradorpython"  # Intentando acceder antes de definir


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# Crea una instancia de la clase Marshmallow y la asigna al objeto ma para trabajar con serialización y deserialización de datos
ma = Marshmallow(app)

# Producto hereda de db.Model


# Cliente
class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    correo_electronico = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    razon_social = db.Column(db.String(100))
    ruc = db.Column(db.Integer)
    telefono = db.Column(db.Integer)
    cuenta_contable = db.relationship("Cuenta_Contable", backref="cliente", lazy=True)

    def __init__(
        self,
        id_cliente,
        correo_electronico,
        direccion,
        nombre,
        razon_social,
        ruc,
        telefono,
    ):
        self.id_cliente = id_cliente
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        self.nombre = nombre
        self.razon_social = razon_social
        self.ruc = ruc
        self.telefono = telefono

    def to_json(self):
        return {
            "id_cliente": self.id_cliente,
            "correo_electronico": self.correo_electronico,
            "direccion": self.direccion,
            "nombre": self.nombre,
            "razon_social": self.razon_social,
            "ruc": self.ruc,
            "telefono": self.telefono,
        }


# Cuenta Contable
class Cuenta_Contable(db.Model):
    id_cuenta = db.Column(db.Integer, primary_key=True)
    cuenta_acreditada = db.Column(db.Integer)
    cuenta_debitada = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    id_cliente = db.Column(db.Integer)
    nombre = db.Column(db.String(100))
    numero_cuenta = db.Column(db.Integer)

    def __init__(
        self,
        id_cuenta,
        cuenta_acreditada,
        cuenta_debitada,
        descripcion,
        id_clientes,
        nombre_cuenta,
        numero_cuenta,
    ):
        self.id_cuenta = id_cuenta
        self.cuenta_acreditada = cuenta_acreditada
        self.cuenta_debitada = cuenta_debitada
        self.descripcion = descripcion
        self.id_clientes = id_clientes
        self.nombre_cuenta = nombre_cuenta
        self.numero_cuenta = numero_cuenta

    def to_json(self):
        return {
            "id_cuenta": self.id_cuenta,
            "cuenta_acreditada": self.cuenta_acreditada,
            "cuenta_debitada": self.cuenta_debitada,
            "descripcion": self.descripcion,
            "id_clientes": self.id_clientes,
            "nombre_cuenta": self.nombre_cuenta,
            "numero_cuenta": self.numero_cuenta,
        }


# Factura
class Factura(db.Model):
    fecha_emision = db.Column(db.Date)
    id_clientes = db.Column(db.Integer)
    id_factura = db.Column(db.Integer, primary_key=True)
    impuestos = db.Column(db.String(100))
    numero_factura = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(
        self,
        fecha_emision,
        id_clientes,
        id_factura,
        impuestos,
        numero_factura,
        subtotal,
        total,
    ):
        self.fecha_emision = fecha_emision
        self.id_clientes = id_clientes
        self.id_factura = id_factura
        self.impuestos = impuestos
        self.numero_factura = numero_factura
        self.subtotal = subtotal
        self.total = total

    def to_json(self):
        return {
            "fecha_emision": str(self.fecha_emision),
            "id_clientes": self.id_clientes,
            "id_factura": self.id_factura,
            "impuestos": self.impuestos,
            "numero_factura": self.numero_factura,
            "subtotal": self.subtotal,
            "total": self.total,
        }


# Libro Mayor
class Libro_Mayor(db.Model):
    credito = db.Column(db.Integer)
    debito = db.Column(db.Integer)
    fecha_registro = db.Column(db.Date)
    id_cuenta_contable = db.Column(db.Integer)
    id_libro_mayor = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Integer)

    def __init__(
        self, credito, debito, fecha_registro, id_cuenta_contable, id_libro_mayor, saldo
    ):
        self.credito = credito
        self.debito = debito
        self.fecha_registro = fecha_registro
        self.id_cuentas_contables = id_cuenta_contable
        self.id_libro_mayor = id_libro_mayor
        self.saldo = saldo

    def to_json(self):
        return {
            "credito": self.credito,
            "debito": self.debito,
            "fecha_registro": str(self.fecha_registro),
            "id_cuenta_contable": self.id_cuenta_contable,
            "id_libro_mayor": self.id_libro_mayor,
            "saldo": self.saldo,
        }


# Orden de Compra
class Orden_Compra(db.Model):
    fecha_emision = db.Column(db.Date)
    id_clientes = db.Column(db.Integer)
    id_orden_compra = db.Column(db.Integer, primary_key=True)
    id_proveedores = db.Column(db.Integer)
    impuestos = db.Column(db.Integer)
    numero_orden = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(
        self,
        fecha_emision,
        id_clientes,
        id_orden_compra,
        id_proveedores,
        impuestos,
        numero_orden,
        subtotal,
        total,
    ):
        self.fecha_emision = fecha_emision
        self.id_clientes = id_clientes
        self.id_orden_compra = id_orden_compra
        self.id_proveedores = id_proveedores
        self.impuestos = impuestos
        self.numero_orden = numero_orden
        self.subtotal = subtotal
        self.total = total

    def to_json(self):
        return {
            "fecha_emision": str(self.fecha_emision),
            "id_clientes": self.id_clientes,
            "id_orden_compra": self.id_orden_compra,
            "id_proveedores": self.id_proveedores,
            "impuestos": self.impuestos,
            "numero_orden": self.numero_orden,
            "subtotal": self.subtotal,
            "total": self.total,
        }


# Proveedores
class Proveedores(db.Model):
    correo_electronico = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    id_proveedores = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    ruc = db.Column(db.Integer)
    telefono = db.Column(db.Integer)

    def __init__(
        self, correo_electronico, direccion, id_proveedores, nombre, ruc, telefono
    ):
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        self.id_proveedores = id_proveedores
        self.nombre = nombre
        self.ruc = ruc
        self.telefono = telefono

    def to_json(self):
        return {
            "correo_electronico": self.correo_electronico,
            "direccion": self.direccion,
            "id_proveedores": self.id_proveedores,
            "nombre": self.nombre,
            "ruc": self.ruc,
            "telefono": self.telefono,
        }


# Transacciones Contables
class Transacciones_contables(db.Model):
    cuenta_acreditada = db.Column(db.Integer)
    cuenta_debitada = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    fecha_transaccion = db.Column(db.Date)
    id_transacciones_contables = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Integer)
    tipo_transaccion = db.Column(db.String(100))

    def __init__(
        self,
        cuenta_acreditada,
        cuenta_debitada,
        descripcion,
        fecha_transaccion,
        id_transacciones_contables,
        monto,
        tipo_transaccion,
    ):
        self.cuenta_acreditada = cuenta_acreditada
        self.cuenta_debitada = cuenta_debitada
        self.descripcion = descripcion
        self.fecha_transaccion = fecha_transaccion
        self.id_transacciones_contables = id_transacciones_contables
        self.monto = monto
        self.tipo_transaccion = tipo_transaccion

    def to_json(self):
        return {
            "cuenta_acreditada": self.cuenta_acreditada,
            "cuenta_debitada": self.cuenta_debitada,
            "descripcion": self.descripcion,
            "fecha_transaccion": str(self.fecha_transaccion),
            "id_transacciones_contables": self.id_transacciones_contables,
            "monto": self.monto,
            "tipo_transaccion": self.tipo_transaccion,
        }

    # ----------------------------------------------
    # Definición del esquema para la clase Cliente


class ClienteSchema(ma.Schema):
    """
    Esquema de la clase Cliente.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Cliente.
    """

    class Meta:
        fields = (
            "id_cliente",
            "correo_electronico",
            "direccion",
            "nombre",
            "razon_social",
            "ruc",
            "telefono",
        )


# Creación de instancias del esquema para serializar/deserializar un cliente
cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)


# ---------------------------------------
# Definición del esquema para la clase Cuenta_Contable
class Cuenta_ContableSchema(ma.Schema):
    """
    Esquema de la clase Cuenta_Contable.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Cuenta_Contable.
    """

    class Meta:
        fields = (
            "id_cuenta",
            "cuenta_acreditada",
            "cuenta_debitada",
            "descripcion",
            "id_cliente",
            "nombre",
            "numero_cuenta",
        )


# Creación de instancias del esquema para serializar/deserializar una cuenta contable
cuenta_contable_schema = Cuenta_ContableSchema()
cuentas_contables_schema = Cuenta_ContableSchema(many=True)


# -------------------------------------------------------
# Definición del esquema para la clase Orden_Compra
class Orden_compraSchema(ma.Schema):
    """
    Esquema de la clase Orden_Compra.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Orden_Compra.
    """

    class Meta:
        fields = (
            "fecha_emision",
            "id_clientes",
            "id_orden_compra",
            "id_proveedores",
            "impuestos",
            "numero_orden",
            "subtotal",
            "total",
        )


# Creación de instancias del esquema para serializar/deserializar una orden de compra
orden_compra_schema = Orden_compraSchema()
ordenes_compra_schema = Orden_compraSchema(many=True)


# -----------------------------------------------------
# Definición del esquema para la clase Factura
class FacturaSchema(ma.Schema):
    """
    Esquema de la clase Factura.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Factura.
    """

    class Meta:
        fields = (
            "fecha_emision",
            "id_clientes",
            "id_factura",
            "impuestos",
            "numero_factura",
            "subtotal",
            "total",
        )


# Creación de instancias del esquema para serializar/deserializar una factura
factura_schema = FacturaSchema()
facturas_schema = FacturaSchema(many=True)


# -----------------------------------------------------
# Definición del esquema para la clase Libro_Mayor
class LibroMayorSchema(ma.Schema):
    """
    Esquema de la clase Libro_Mayor.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Libro_Mayor.
    """

    class Meta:
        fields = (
            "credito",
            "debito",
            "fecha_registro",
            "id_cuenta_contable",
            "id_libro_mayor",
            "saldo",
        )


# Creación de instancias del esquema para serializar/deserializar un libro mayor
libro_mayor_schema = LibroMayorSchema()
libros_mayor_schema = LibroMayorSchema(many=True)


# -------------------------------------------------
# Definición del esquema para la clase Proveedores
class ProveedoresSchema(ma.Schema):
    """
    Esquema de la clase Proveedores.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Proveedores.
    """

    class Meta:
        fields = (
            "correo_electronico",
            "direccion",
            "id_proveedores",
            "nombre",
            "ruc",
            "telefono",
        )


# Creación de instancias del esquema para serializar/deserializar un proveedor
proveedor_schema = ProveedoresSchema()
proveedores_schema = ProveedoresSchema(many=True)


# --------------------------------------------
# Definición del esquema para la clase TransaccionesContables
class TransaccionesContablesSchema(ma.Schema):
    """
    Esquema de la clase TransaccionesContables.

    Este esquema define los campos que serán serializados/deserializados
    para la clase TransaccionesContables.
    """

    class Meta:
        fields = (
            "cuenta_acreditada",
            "cuenta_debitada",
            "descripcion",
            "fecha_transaccion",
            "id_transacciones_contables",
            "monto",
            "tipo_transaccion",
        )


# Creación de instancias del esquema para serializar/deserializar una transacción contable
transaccion_contable_schema = TransaccionesContablesSchema()
transacciones_contables_schema = TransaccionesContablesSchema(many=True)




# Se pueden agregar más clases para definir otras tablas en la base de datos

with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos


@app.route("/cliente/<id>", methods=["GET"])
def get_cliente(id):
    """
    Endpoint para obtener un cliente específico de la base de datos.

    Retorna un JSON con la información del cliente correspondiente al ID proporcionado.
    """
    cliente = Cliente.query.get(id)
    return cliente.to_json()


@app.route("/cliente/<id>", methods=["DELETE"])
def delete_cliente(id):
    """
    Endpoint para eliminar un cliente de la base de datos.

    Elimina el cliente correspondiente al ID proporcionado y retorna un JSON con el registro eliminado.
    """
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return cliente.to_json()


@app.route("/cliente", methods=["POST"])
def create_cliente():
    """
    Endpoint para crear un nuevo cliente en la base de datos.

    Lee los datos proporcionados en formato JSON por el cliente y crea un nuevo registro de cliente en la base de datos.
    Retorna un JSON con el nuevo cliente creado.
    """
    # Lee los datos del JSON
    correo_electronico = request.json["correo_electronico"]
    direccion = request.json["direccion"]
    nombre = request.json["nombre"]
    razon_social = request.json["razon_social"]
    ruc = request.json["ruc"]
    telefono = request.json["telefono"]

    # Crea un nuevo objeto Cliente con los datos proporcionados
    new_cliente = Cliente(
        correo_electronico, direccion, nombre, razon_social, ruc, telefono
    )

    # Agrega el nuevo cliente a la sesión de la base de datos
    db.session.add(new_cliente)
    db.session.commit()

    return new_cliente.to_json()


@app.route("/cliente/<id>", methods=["PUT"])
def update_cliente(id):
    """
    Endpoint para actualizar un cliente existente en la base de datos.

    Lee los datos proporcionados en formato JSON por el cliente y actualiza el registro del cliente con el ID especificado.
    Retorna un JSON con el cliente actualizado.
    """
    cliente = Cliente.query.get(id)

    # Actualiza los atributos del cliente con los datos proporcionados en el JSON
    cliente.correo_electronico = request.json["correo_electronico"]
    cliente.direccion = request.json["direccion"]
    cliente.nombre = request.json["nombre"]
    cliente.razon_social = request.json["razon_social"]
    cliente.ruc = request.json["ruc"]
    cliente.telefono = request.json["telefono"]

    db.session.commit()
    return cliente.to_json()


# ------------------------------------------------------------
@app.route("/cuenta_contable/<id>", methods=["GET"])
def get_cuenta_contable(id):
    cuenta_contable = Cuenta_Contable.query.get(id)
    return cuenta_contable.to_json()


@app.route("/cuenta_contable/<id>", methods=["DELETE"])
def delete_cuenta_contable(id):
    cuenta_contable = Cuenta_Contable.query.get(id)
    db.session.delete(cuenta_contable)
    db.session.commit()
    return cuenta_contable.to_json()


@app.route("/cuenta_contable", methods=["POST"])
def create_cuenta_contable():
    cuenta_acreditada = request.json["cuenta_acreditada"]
    cuenta_debitada = request.json["cuenta_debitada"]
    descripcion = request.json["descripcion"]
    id_clientes = request.json["id_clientes"]
    nombre_cuenta = request.json["nombre_cuenta"]
    numero_cuenta = request.json["numero_cuenta"]

    nueva_cuenta_contable = Cuenta_Contable(
        cuenta_acreditada=cuenta_acreditada,
        cuenta_debitada=cuenta_debitada,
        descripcion=descripcion,
        id_clientes=id_clientes,
        nombre_cuenta=nombre_cuenta,
        numero_cuenta=numero_cuenta,
    )

    db.session.add(nueva_cuenta_contable)
    db.session.commit()

    return nueva_cuenta_contable.to_json()


@app.route("/cuenta_contable/<id>", methods=["PUT"])
def update_cuenta_contable(id):
    cuenta_contable = Cuenta_Contable.query.get(id)

    cuenta_contable.cuenta_acreditada = request.json["cuenta_acreditada"]
    cuenta_contable.cuenta_debitada = request.json["cuenta_debitada"]
    cuenta_contable.descripcion = request.json["descripcion"]
    cuenta_contable.id_clientes = request.json["id_clientes"]
    cuenta_contable.nombre_cuenta = request.json["nombre_cuenta"]
    cuenta_contable.numero_cuenta = request.json["numero_cuenta"]

    db.session.commit()
    return cuenta_contable.to_json()
    # ----------------------------------------------------


# Facturas
@app.route("/factura/<id>", methods=["GET"])
def get_factura(id):
    factura = Factura.query.get(id)
    return factura.to_json()


@app.route("/factura/<id>", methods=["DELETE"])
def delete_factura(id):
    factura = Factura.query.get(id)
    db.session.delete(factura)
    db.session.commit()
    return factura.to_json()


@app.route("/factura", methods=["POST"])
def create_factura():
    data = request.json
    nueva_factura = Factura(
        fecha_emision=data["fecha_emision"],
        id_clientes=data["id_clientes"],
        impuestos=data["impuestos"],
        numero_factura=data["numero_factura"],
        subtotal=data["subtotal"],
        total=data["total"],
    )
    db.session.add(nueva_factura)
    db.session.commit()
    return nueva_factura.to_json()


@app.route("/factura/<id>", methods=["PUT"])
def update_factura(id):
    factura = Factura.query.get(id)
    data = request.json
    factura.fecha_emision = data["fecha_emision"]
    factura.id_clientes = data["id_clientes"]
    factura.impuestos = data["impuestos"]
    factura.numero_factura = data["numero_factura"]
    factura.subtotal = data["subtotal"]
    factura.total = data["total"]
    db.session.commit()
    return factura.to_json()


# Libro Mayor
@app.route("/libro_mayor/<id>", methods=["GET"])
def get_libro_mayor(id):
    registro_libro_mayor = Libro_Mayor.query.get(id)
    return registro_libro_mayor.to_json()


@app.route("/libro_mayor/<id>", methods=["DELETE"])
def delete_libro_mayor(id):
    registro_libro_mayor = Libro_Mayor.query.get(id)
    db.session.delete(registro_libro_mayor)
    db.session.commit()
    return registro_libro_mayor.to_json()


@app.route("/libro_mayor", methods=["POST"])
def create_libro_mayor():
    data = request.json
    nuevo_registro_libro_mayor = Libro_Mayor(
        credito=data["credito"],
        debito=data["debito"],
        fecha_registro=data["fecha_registro"],
        id_cuentas_contables=data["id_cuentas_contables"],
        saldo=data["saldo"],
    )
    db.session.add(nuevo_registro_libro_mayor)
    db.session.commit()
    return nuevo_registro_libro_mayor.to_json()


@app.route("/libro_mayor/<id>", methods=["PUT"])
def update_libro_mayor(id):
    registro_libro_mayor = Libro_Mayor.query.get(id)
    data = request.json
    registro_libro_mayor.credito = data["credito"]
    registro_libro_mayor.debito = data["debito"]
    registro_libro_mayor.fecha_registro = data["fecha_registro"]
    registro_libro_mayor.id_cuentas_contables = data["id_cuentas_contables"]
    registro_libro_mayor.saldo = data["saldo"]
    db.session.commit()
    return registro_libro_mayor.to_json()


# Órdenes de Compra
@app.route("/orden_compra/<id>", methods=["DELETE"])
def delete_orden_compra(id):
    orden_compra = Orden_Compra.query.get(id)
    db.session.delete(orden_compra)
    db.session.commit()
    return orden_compra.to_json()


@app.route("/orden_compra", methods=["POST"])
def create_orden_compra():
    data = request.json
    nueva_orden_compra = Orden_Compra(
        fecha_emision=data["fecha_emision"],
        id_clientes=data["id_clientes"],
        id_proveedores=data["id_proveedores"],
        impuestos=data["impuestos"],
        numero_orden=data["numero_orden"],
        subtotal=data["subtotal"],
        total=data["total"],
    )
    db.session.add(nueva_orden_compra)
    db.session.commit()
    return nueva_orden_compra.to_json()


@app.route("/orden_compra/<id>", methods=["PUT"])
def update_orden_compra(id):
    orden_compra = Orden_Compra.query.get(id)
    data = request.json
    orden_compra.fecha_emision = data["fecha_emision"]
    orden_compra.id_clientes = data["id_clientes"]
    orden_compra.id_proveedores = data["id_proveedores"]
    orden_compra.impuestos = data["impuestos"]
    orden_compra.numero_orden = data["numero_orden"]
    orden_compra.subtotal = data["subtotal"]
    orden_compra.total = data["total"]
    db.session.commit()
    return orden_compra.to_json()


# Proveedores
@app.route("/proveedores/<id>", methods=["GET"])
def get_proveedor(id):
    proveedor = Proveedores.query.get(id)
    return proveedor.to_json()


@app.route("/proveedores/<id>", methods=["DELETE"])
def delete_proveedor(id):
    proveedor = Proveedores.query.get(id)
    db.session.delete(proveedor)
    db.session.commit()
    return proveedor.to_json()


@app.route("/proveedores", methods=["POST"])
def create_proveedor():
    data = request.json
    nuevo_proveedor = Proveedores(
        correo_electronico=data["correo_electronico"],
        direccion=data["direccion"],
        nombre=data["nombre"],
        ruc=data["ruc"],
        telefono=data["telefono"],
    )
    db.session.add(nuevo_proveedor)
    db.session.commit()
    return nuevo_proveedor.to_json()


@app.route("/proveedores/<id>", methods=["PUT"])
def update_proveedor(id):
    proveedor = Proveedores.query.get(id)
    data = request.json
    proveedor.correo_electronico = data["correo_electronico"]
    proveedor.direccion = data["direccion"]
    proveedor.nombre = data["nombre"]
    proveedor.ruc = data["ruc"]
    proveedor.telefono = data["telefono"]
    db.session.commit()
    return proveedor.to_json()


# Transacciones Contables
@app.route("/transacciones_contables/<id>", methods=["GET"])
def get_transaccion_contable(id):
    transaccion_contable = Transacciones_contables.query.get(id)
    return transaccion_contable.to_json()


@app.route("/transacciones_contables/<id>", methods=["DELETE"])
def delete_transaccion_contable(id):
    transaccion_contable = Transacciones_contables.query.get(id)
    db.session.delete(transaccion_contable)
    db.session.commit()
    return transaccion_contable.to_json()


@app.route("/transacciones_contables", methods=["POST"])
def create_transaccion_contable():
    data = request.json
    nueva_transaccion_contable = Transacciones_contables(
        cuenta_acreditada=data["cuenta_acreditada"],
        cuenta_debitada=data["cuenta_debitada"],
        descripcion=data["descripcion"],
        fecha_transaccion=data["fecha_transaccion"],
        monto=data["monto"],
        tipo_transaccion=data["tipo_transaccion"],
    )
    db.session.add(nueva_transaccion_contable)
    db.session.commit()
    return nueva_transaccion_contable.to_json()


@app.route("/transacciones_contables/<id>", methods=["PUT"])
def update_transaccion_contable(id):
    transaccion_contable = Transacciones_contables.query.get(id)
    data = request.json
    transaccion_contable.cuenta_acreditada = data["cuenta_acreditada"]
    transaccion_contable.cuenta_debitada = data["cuenta_debitada"]
    transaccion_contable.descripcion = data["descripcion"]
    transaccion_contable.fecha_transaccion = data["fecha_transaccion"]
    transaccion_contable.monto = data["monto"]
    transaccion_contable.tipo_transaccion = data["tipo_transaccion"]
    db.session.commit()
    return transaccion_contable.to_json()

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


# Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)
