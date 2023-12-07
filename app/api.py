from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configura la conexión a la base de datos
config = {
    'user': 'root',
    'host': 'localhost',
    'database': 'contabilidaddb',
}

# Crea la conexión
conexion = mysql.connector.connect(**config)

# Crea un cursor para ejecutar consultas
cursor = conexion.cursor()

# Modelar los datos
class Cliente:
    def __init__(self, id_cliente, correo_electronico, direccion, nombre, razon_social, ruc, telefono):
        self.id_cliente = id_cliente
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        self.nombre = nombre
        self.razon_social = razon_social
        self.ruc = ruc
        self.telefono = telefono

class CuentaContable:
    def __init__(self, id_cuenta, cuenta_acreditada, cuenta_debitada, descripcion, id_clientes, nombre_cuenta, numero_cuenta):
        self.id_cuenta = id_cuenta
        self.cuenta_acreditada = cuenta_acreditada
        self.cuenta_debitada = cuenta_debitada
        self.descripcion = descripcion
        self.id_clientes = id_clientes
        self.nombre_cuenta = nombre_cuenta
        self.numero_cuenta = numero_cuenta

class Factura:
    def __init__(self, fecha_emision, id_clientes, id_factura, impuestos, numero_factura, subtotal, total):
        self.fecha_emision = fecha_emision
        self.id_clientes = id_clientes
        self.id_factura = id_factura
        self.impuestos = impuestos
        self.numero_factura = numero_factura
        self.subtotal = subtotal
        self.total = total

class LibroMayor:
    def __init__(self, credito, debito, fecha_registro, id_cuentas_contables, id_libro_mayor, saldo):
        self.credito = credito
        self.debito = debito
        self.fecha_registro = fecha_registro
        self.id_cuentas_contables = id_cuentas_contables
        self.id_libro_mayor = id_libro_mayor
        self.saldo = saldo

class OrdenCompra:
    def __init__(self, fecha_emision, id_clientes, id_ordenes_compra, id_proveedores, impuestos, numero_orden, subtotal, total):
        self.fecha_emision = fecha_emision
        self.id_clientes = id_clientes
        self.id_ordenes_compra = id_ordenes_compra
        self.id_proveedores = id_proveedores
        self.impuestos = impuestos
        self.numero_orden = numero_orden
        self.subtotal = subtotal
        self.total = total

class Proveedor:
    def __init__(self, correo_electronico, direccion, id_proveedores, nombre, ruc, telefono):
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        self.id_proveedores = id_proveedores
        self.nombre = nombre
        self.ruc = ruc
        self.telefono = telefono

class TransaccionContable:
    def __init__(self, cuenta_acreditada, cuenta_debitada, descripcion, fecha_transaccion, id_transacciones_contables, monto, tipo_transaccion):
        self.cuenta_acreditada = cuenta_acreditada
        self.cuenta_debitada = cuenta_debitada
        self.descripcion = descripcion
        self.fecha_transaccion = fecha_transaccion
        self.id_transacciones_contables = id_transacciones_contables
        self.monto = monto
        self.tipo_transaccion = tipo_transaccion

# Rutas para la API
# Rutas para la API
@app.route('/transaccionescontables', methods=['GET', 'POST'])
def transacciones_contables():
    if request.method == 'GET':
        consulta = "SELECT * FROM transaccionescontables"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        transacciones_contables = [{'cuenta_acreditada': fila[0],
                                    'cuenta_debitada': fila[1],
                                    'descripcion': fila[2],
                                    'fecha_transaccion': fila[3],
                                    'id_transacciones_contables': fila[4],
                                    'monto': fila[5],
                                    'tipo_transaccion': fila[6]
                                    } for fila in resultados]
        return jsonify(transacciones_contables)
    elif request.method == 'POST':
        datos_transaccion_contable = request.json
        nueva_transaccion_contable = TransaccionContable(**datos_transaccion_contable)

        consulta = "INSERT INTO transaccionescontables (cuentaAcreditada, cuentadebitada, descripcion, fechatransaccion, idtransaccionescontables, monto, tipotransaccion) " \
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        valores = (nueva_transaccion_contable.cuenta_acreditada, nueva_transaccion_contable.cuenta_debitada,
                   nueva_transaccion_contable.descripcion, nueva_transaccion_contable.fecha_transaccion,
                   nueva_transaccion_contable.id_transacciones_contables, nueva_transaccion_contable.monto,
                   nueva_transaccion_contable.tipo_transaccion)

        cursor.execute(consulta, valores)
        conexion.commit()

        return jsonify({'id_transacciones_contables': nueva_transaccion_contable.id_transacciones_contables}), 201

@app.route('/transaccionescontables/<int:id_transaccion>', methods=['PUT', 'DELETE'])
def modificar_eliminar_transaccion_contable(id_transaccion):
    if request.method == 'PUT':
        datos_transaccion_contable = request.json

        consulta = "UPDATE transaccionescontables SET cuentaAcreditada=%s, cuentadebitada=%s, descripcion=%s, fechatransaccion=%s, monto=%s, tipotransaccion=%s " \
                   "WHERE idtransaccionescontables = %s"
        
        valores = (datos_transaccion_contable['cuenta_acreditada'], datos_transaccion_contable['cuenta_debitada'],
                   datos_transaccion_contable['descripcion'], datos_transaccion_contable['fecha_transaccion'],
                   datos_transaccion_contable['monto'], datos_transaccion_contable['tipo_transaccion'], id_transaccion)

        cursor.execute(consulta, valores)
        conexion.commit()

        return jsonify({'mensaje': 'Transacción contable modificada correctamente'})
    elif request.method == 'DELETE':
        consulta = "DELETE FROM transaccionescontables WHERE idtransaccionescontables = %s"
        cursor.execute(consulta, (id_transaccion,))
        conexion.commit()

        return jsonify({'mensaje': 'Transacción contable eliminada correctamente'})


# Agrega rutas para actualizar y eliminar transacciones_contables según tus necesidades

# Ruta para obtener, crear, actualizar y eliminar clientes
@app.route('/clientes', methods=['GET', 'POST'])
def gestionar_clientes():
    if request.method == 'GET':
        consulta = "SELECT * FROM clientes"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        clientes = [{'id_cliente': fila[0],
                     'correo_electronico': fila[1],
                     'direccion': fila[2],
                     'nombre': fila[3],
                     'razon_social': fila[4],
                     'ruc': fila[5],
                     'telefono': fila[6]} for fila in resultados]
        return jsonify(clientes)
    elif request.method == 'POST':
        datos_cliente = request.json
        nuevo_cliente = Cliente(**datos_cliente)

        consulta = "INSERT INTO clientes (correo_electronico, direccion, nombre, razon_social, ruc, telefono) " \
                   "VALUES (%s, %s, %s, %s, %s, %s)"
        
        valores = (nuevo_cliente.correo_electronico, nuevo_cliente.direccion, nuevo_cliente.nombre,
                   nuevo_cliente.razon_social, nuevo_cliente.ruc, nuevo_cliente.telefono)

        cursor.execute(consulta, valores)
        conexion.commit()

        return jsonify({'id_cliente': cursor.lastrowid}), 201

@app.route('/clientes/<int:id_cliente>', methods=['GET', 'PUT', 'DELETE'])
def gestionar_cliente(id_cliente):
    if request.method == 'GET':
        consulta = "SELECT * FROM clientes WHERE id_cliente = %s"
        cursor.execute(consulta, (id_cliente,))
        resultado = cursor.fetchone()
        if resultado:
            cliente = {'id_cliente': resultado[0],
                       'correo_electronico': resultado[1],
                       'direccion': resultado[2],
                       'nombre': resultado[3],
                       'razon_social': resultado[4],
                       'ruc': resultado[5],
                       'telefono': resultado[6]}
            return jsonify(cliente)
        else:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
    elif request.method == 'PUT':
        datos_cliente = request.json

        consulta = "UPDATE clientes SET correo_electronico=%s, direccion=%s, nombre=%s, razon_social=%s, ruc=%s, telefono=%s " \
                   "WHERE id_cliente = %s"
        
        valores = (datos_cliente['correo_electronico'], datos_cliente['direccion'], datos_cliente['nombre'],
                   datos_cliente['razon_social'], datos_cliente['ruc'], datos_cliente['telefono'], id_cliente)

        cursor.execute(consulta, valores)
        conexion.commit()

        return jsonify({'mensaje': 'Cliente actualizado correctamente'})
    elif request.method == 'DELETE':
        consulta = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(consulta, (id_cliente,))
        conexion.commit()

        return jsonify({'mensaje': 'Cliente eliminado correctamente'})

# Repite el mismo patrón para cada entidad (CuentaContable, Factura, LibroMayor, OrdenCompra, Proveedor, TransaccionContable)
# Crear rutas adicionales para obtener, crear, actualizar y eliminar registros en cada tabla.
@app.route('/cuentascontables/<int:id_cuenta>', methods=['GET'])
def obtener_cuenta_contable(id_cuenta):
    consulta = "SELECT * FROM cuentascontables WHERE id_cuenta = %s"
    cursor.execute(consulta, (id_cuenta,))
    resultado = cursor.fetchone()
    if resultado:
        cuenta_contable = {'id_cuenta': resultado[0],
                           'cuenta_acreditada': resultado[1],
                           'cuenta_debitada': resultado[2],
                           'descripcion': resultado[3],
                           'id_clientes': resultado[4],
                           'nombre_cuenta': resultado[5],
                           'numero_cuenta': resultado[6]}
        return jsonify(cuenta_contable)
    else:
        return jsonify({'mensaje': 'Cuenta Contable no encontrada'}), 404

@app.route('/cuentascontables', methods=['POST'])
def crear_cuenta_contable():
    datos_cuenta_contable = request.json
    nueva_cuenta_contable = CuentaContable(**datos_cuenta_contable)

    consulta = "INSERT INTO cuentascontables (cuenta_acreditada, cuenta_debitada, descripcion, id_clientes, nombre_cuenta, numero_cuenta) " \
               "VALUES (%s, %s, %s, %s, %s, %s)"
    
    valores = (nueva_cuenta_contable.cuenta_acreditada, nueva_cuenta_contable.cuenta_debitada,
               nueva_cuenta_contable.descripcion, nueva_cuenta_contable.id_clientes,
               nueva_cuenta_contable.nombre_cuenta, nueva_cuenta_contable.numero_cuenta)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'id_cuenta': cursor.lastrowid}), 201

@app.route('/cuentascontables/<int:id_cuenta>', methods=['PUT'])
def actualizar_cuenta_contable(id_cuenta):
    datos_cuenta_contable = request.json

    consulta = "UPDATE cuentascontables SET cuenta_acreditada=%s, cuenta_debitada=%s, descripcion=%s, id_clientes=%s, nombre_cuenta=%s, numero_cuenta=%s " \
               "WHERE id_cuenta = %s"
    
    valores = (datos_cuenta_contable['cuenta_acreditada'], datos_cuenta_contable['cuenta_debitada'],
               datos_cuenta_contable['descripcion'], datos_cuenta_contable['id_clientes'],
               datos_cuenta_contable['nombre_cuenta'], datos_cuenta_contable['numero_cuenta'], id_cuenta)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'mensaje': 'Cuenta Contable actualizada correctamente'})

@app.route('/cuentascontables/<int:id_cuenta>', methods=['DELETE'])
def eliminar_cuenta_contable(id_cuenta):
    consulta = "DELETE FROM cuentascontables WHERE id_cuenta = %s"
    cursor.execute(consulta, (id_cuenta,))
    conexion.commit()

    return jsonify({'mensaje': 'Cuenta Contable eliminada correctamente'})
# metodos proveedores
# Rutas adicionales para modificar, crear y eliminar proveedores

@app.route('/proveedores/<int:id_proveedor>', methods=['PUT'])
def modificar_proveedor(id_proveedor):
    datos_proveedor = request.json

    consulta = "UPDATE proveedores SET correoelectronico=%s, direccion=%s, nombre=%s, ruc=%s, telefono=%s " \
               "WHERE idProveedores = %s"
    
    valores = (datos_proveedor['correo_electronico'], datos_proveedor['direccion'], datos_proveedor['nombre'],
               datos_proveedor['ruc'], datos_proveedor['telefono'], id_proveedor)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'mensaje': 'Proveedor modificado correctamente'})

@app.route('/proveedores', methods=['POST'])
def crear_proveedor():
    datos_proveedor = request.json
    nuevo_proveedor = Proveedor(**datos_proveedor)

    consulta = "INSERT INTO proveedores (correoelectronico, direccion, idProveedores, nombre, ruc, telefono) " \
               "VALUES (%s, %s, %s, %s, %s, %s)"
    
    valores = (nuevo_proveedor.correo_electronico, nuevo_proveedor.direccion, nuevo_proveedor.id_proveedores,
               nuevo_proveedor.nombre, nuevo_proveedor.ruc, nuevo_proveedor.telefono)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'id_proveedores': nuevo_proveedor.id_proveedores}), 201

@app.route('/proveedores/<int:id_proveedor>', methods=['DELETE'])
def eliminar_proveedor(id_proveedor):
    consulta = "DELETE FROM proveedores WHERE idProveedores = %s"
    cursor.execute(consulta, (id_proveedor,))
    conexion.commit()

    return jsonify({'mensaje': 'Proveedor eliminado correctamente'})
#metodos para facturacion 
# Rutas adicionales para modificar, crear y eliminar facturas

@app.route('/facturas/<int:id_factura>', methods=['PUT'])
def modificar_factura(id_factura):
    datos_factura = request.json

    consulta = "UPDATE facturas SET fechaemision=%s, idclientes=%s, impuestos=%s, numerofactura=%s, subtotal=%s, total=%s " \
               "WHERE idFactura = %s"
    
    valores = (datos_factura['fecha_emision'], datos_factura['id_clientes'], datos_factura['impuestos'],
               datos_factura['numero_factura'], datos_factura['subtotal'], datos_factura['total'], id_factura)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'mensaje': 'Factura modificada correctamente'})

@app.route('/facturas', methods=['POST'])
def crear_factura():
    datos_factura = request.json
    nueva_factura = Factura(**datos_factura)

    consulta = "INSERT INTO facturas (fechaemision, idclientes, idFactura, impuestos, numerofactura, subtotal, total) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    valores = (nueva_factura.fecha_emision, nueva_factura.id_clientes, nueva_factura.id_factura,
               nueva_factura.impuestos, nueva_factura.numero_factura, nueva_factura.subtotal, nueva_factura.total)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'id_factura': nueva_factura.id_factura}), 201

@app.route('/facturas/<int:id_factura>', methods=['DELETE'])
def eliminar_factura(id_factura):
    consulta = "DELETE FROM facturas WHERE idFactura = %s"
    cursor.execute(consulta, (id_factura,))
    conexion.commit()

    return jsonify({'mensaje': 'Factura eliminada correctamente'})
#metodo para libro mayor
# Rutas adicionales para crear, modificar y eliminar registros en el Libro Mayor

@app.route('/libromayor', methods=['POST'])
def crear_libro_mayor():
    datos_libro_mayor = request.json
    nuevo_libro_mayor = LibroMayor(**datos_libro_mayor)

    consulta = "INSERT INTO libromayor (credito, debito, fecharegistro, idcuentascontables, idlibromayor, saldo) " \
               "VALUES (%s, %s, %s, %s, %s, %s)"
    
    valores = (nuevo_libro_mayor.credito, nuevo_libro_mayor.debito, nuevo_libro_mayor.fecha_registro,
               nuevo_libro_mayor.id_cuentas_contables, nuevo_libro_mayor.id_libro_mayor, nuevo_libro_mayor.saldo)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'id_libro_mayor': nuevo_libro_mayor.id_libro_mayor}), 201

@app.route('/libromayor/<int:id_libro_mayor>', methods=['PUT'])
def modificar_libro_mayor(id_libro_mayor):
    datos_libro_mayor = request.json

    consulta = "UPDATE libromayor SET credito=%s, debito=%s, fecharegistro=%s, idcuentascontables=%s, saldo=%s " \
               "WHERE idlibromayor = %s"
    
    valores = (datos_libro_mayor['credito'], datos_libro_mayor['debito'], datos_libro_mayor['fecha_registro'],
               datos_libro_mayor['id_cuentas_contables'], datos_libro_mayor['saldo'], id_libro_mayor)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'mensaje': 'Registro en el Libro Mayor modificado correctamente'})

@app.route('/libromayor/<int:id_libro_mayor>', methods=['DELETE'])
def eliminar_libro_mayor(id_libro_mayor):
    consulta = "DELETE FROM libromayor WHERE idlibromayor = %s"
    cursor.execute(consulta, (id_libro_mayor,))
    conexion.commit()

    return jsonify({'mensaje': 'Registro en el Libro Mayor eliminado correctamente'})
#metodos para orden de compra 
# Rutas adicionales para crear, modificar y eliminar Orden de Compra

@app.route('/ordenescompra', methods=['POST'])
def crear_orden_compra():
    datos_orden_compra = request.json
    nueva_orden_compra = OrdenCompra(**datos_orden_compra)

    consulta = "INSERT INTO ordenescompra (fechaemision, idclientes, idordenescompra, idproveedores, impuestos, numeroorden, subtotal, total) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    
    valores = (nueva_orden_compra.fecha_emision, nueva_orden_compra.id_clientes, nueva_orden_compra.id_ordenes_compra,
               nueva_orden_compra.id_proveedores, nueva_orden_compra.impuestos, nueva_orden_compra.numero_orden,
               nueva_orden_compra.subtotal, nueva_orden_compra.total)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'id_ordenes_compra': nueva_orden_compra.id_ordenes_compra}), 201

@app.route('/ordenescompra/<int:id_orden_compra>', methods=['PUT'])
def modificar_orden_compra(id_orden_compra):
    datos_orden_compra = request.json

    consulta = "UPDATE ordenescompra SET fechaemision=%s, idclientes=%s, idproveedores=%s, impuestos=%s, numeroorden=%s, " \
               "subtotal=%s, total=%s WHERE idordenescompra = %s"
    
    valores = (datos_orden_compra['fecha_emision'], datos_orden_compra['id_clientes'], datos_orden_compra['id_proveedores'],
               datos_orden_compra['impuestos'], datos_orden_compra['numero_orden'], datos_orden_compra['subtotal'],
               datos_orden_compra['total'], id_orden_compra)

    cursor.execute(consulta, valores)
    conexion.commit()

    return jsonify({'mensaje': 'Orden de Compra modificada correctamente'})

@app.route('/ordenescompra/<int:id_orden_compra>', methods=['DELETE'])
def eliminar_orden_compra(id_orden_compra):
    consulta = "DELETE FROM ordenescompra WHERE idordenescompra = %s"
    cursor.execute(consulta, (id_orden_compra,))
    conexion.commit()

    return jsonify({'mensaje': 'Orden de Compra eliminada correctamente'})
# Ruta para obtener la lista de órdenes de compra en orden ascendente por ID
@app.route('/ordenescompra/listar', methods=['GET'])
def listar_ordenes_compra():
    consulta = "SELECT * FROM ordenescompra ORDER BY idordenescompra ASC"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    
    ordenes_compra = [{'fecha_emision': fila[0],
                       'id_clientes': fila[1],
                       'id_ordenes_compra': fila[2],
                       'id_proveedores': fila[3],
                       'impuestos': fila[4],
                       'numero_orden': fila[5],
                       'subtotal': fila[6],
                       'total': fila[7]
                    } for fila in resultados]

    return jsonify(ordenes_compra)



# Iniciar la aplicación web
if __name__ == '__main__':
    app.run(debug=True)










