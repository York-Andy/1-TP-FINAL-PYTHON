import Vue from 'vue';

document.getElementById("header").innerHTML = `
<nav class="navbar navbar-expand-sm navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="index.html">Navbar</a>
        <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse"
                data-bs-target="#collapsibleNavId" aria-controls="collapsibleNavId"
                aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavId">
            <ul class="navbar-nav me-auto mt-2 mt-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" href="index.html" aria-current="page">Home <span
                            class="visually-hidden">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="dropdownId"
                       data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">CRUD</a>
                    <div class="dropdown-menu" aria-labelledby="dropdownId">
                        <a class="dropdown-item" href="cliente.html">Cliente</a>
                        <a class="dropdown-item" href="cliente_nuevo.html">Cliente_nuevo</a>
                        <a class="dropdown-item" href="clienteUpdate.html">ClienteUpdate</a>
                        <a class="dropdown-item" href="cuentasContable.html">Cuenta_contable</a>
                        <a class="dropdown-item" href="cuentaContable_nuevo.html">CuentaContable_nuevo</a>
                        <a class="dropdown-item" href="cuentaContable_Upade.html">CuentaConatable-upade</a>
                        <a class="dropdown-item" href="ordenesCompra.html">Ordenescompra</a>
                        <a class="dropdown-item" href="ordenCompra_nueva.html">OrdenCompra_nueva</a>
                        <a class="dropdown-item" href="ordenCompraUpdate.html">OrdencompraUpdate</a>
                        <a class="dropdown-item" href="facturas.html">Facturas</a>
                        <a class="dropdown-item" href="facturas_nuevas.html">Facturas_nuevas</a>
                        <a class="dropdown-item" href="facturaUpade.html">FacturaUpade</a>
                        <a class="dropdown-item" href="libroMayor.html">LibroMayor</a>
                        <a class="dropdown-item" href="libroMayor_nuevo.html">LibroMayor_nuevo</a>
                        <a class="dropdown-item" href="libromayorUpdate.html">LibroMayorUpdate</a>
                        <a class="dropdown-item" href="proveedores.html">Proveedores</a>
                        <a class="dropdown-item" href="proveedores_nuevo.html">Proveedores_nuevo</a>
                        <a class="dropdown-item" href="proveedoresUpdate.html">ProveedoresUpdate</a>
                        <a class="dropdown-item" href="index.html">Index</a>
                        <a class="dropdown-item" href="#">Action 2</a>
                    </div>
                </li>
            </ul>
            <form class="d-flex my-2 my-lg-0">
                <input class="form-control me-sm-2" type="text" placeholder="Search">
                <button class="btn btn-outline-success my-2 my-sm-0"
                        type="submit">Search</button>
            </form>
        </div>
    </div>
</nav>`;

const app = new Vue({
    el: '#app',
    data: {
      nombre: '',
      correo_electronico: '',
      direccion: '',
      razon_social: '',
      ruc: '',
      telefono: '',
    },
    methods: {
      grabar() {
        // Validar los campos y realizar la llamada al backend para crear un nuevo cliente
        if (this.nombre && this.correo_electronico && this.direccion && this.ruc && this.telefono) {
          // Lógica para enviar datos al backend (por ejemplo, usando Axios)
          // Aquí puedes hacer una solicitud POST al endpoint correspondiente
  
          // Ejemplo con Axios (asegúrate de incluir la biblioteca en tu proyecto)
           axios.post('/api/clientes', {
             nombre: this.nombre,
             correo: this.correo_electronico,
             direccion:this.direccion,
             razon_social:this.razon_social,
             ruc:this.ruc,
             telefono:this.telefono,
           })
           .then(response => {
            console.log('Cliente creado con éxito:', response.data);
          //   // Realizar otras acciones si es necesario
           })
           .catch(error => {
          //   console.error('Error al crear el cliente:', error);
           });
        } else {
          alert('Por favor, completa todos los campos antes de grabar.');
        }
      }
      // Puedes agregar más métodos para otras operaciones CRUD según tus necesidades
    }
  });





