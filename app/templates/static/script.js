// Funciones para interactuar con la base de datos contabilidaddb

// Función para realizar una solicitud GET a la API para obtener clientes
function obtenerClientes() {
  // Cambiar la URL de la solicitud a la base de datos
  fetch('http://localhost/contabilidaddb/api/clientes', {
    credentials: 'include'
  })
    .then(response => response.json())
    .then(data => {
      // Modificar el código para procesar los datos de la base de datos
      document.getElementById('resultadoClientes').innerHTML = `
        <table class="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Correo electrónico</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            ${data.map(cliente => `
              <tr>
                <td>${cliente.id}</td>
                <td>${cliente.nombre}</td>
                <td>${cliente.correo_electronico}</td>
                <td>
                  <button type="button" class="btn btn-warning" onclick="abrirModalModificar(${cliente.id})">Modificar</button>
                  <button type="button" class="btn btn-danger" onclick="eliminarCliente(${cliente.id})">Eliminar</button>
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;
    })
    .catch(error => {
      console.error('Error al obtener clientes:', error);
    });
}

// Función para abrir un modal para modificar un cliente
function abrirModalModificar(idCliente) {
  // Cargar los datos del cliente en el modal
  const cliente = obtenerClientePorID(idCliente);
  document.getElementById('modal-modificar').querySelector('#id').value = cliente.id;
  document.getElementById('modal-modificar').querySelector('#nombre').value = cliente.nombre;
  document.getElementById('modal-modificar').querySelector('#correo').value = cliente.correo_electronico;

  // Mostrar el modal
  document.getElementById('modal-modificar').classList.add('show');
}

// Función para eliminar un cliente
function eliminarCliente(idCliente) {
  // Eliminar el cliente de la base de datos
  fetch(`http://localhost/contabilidaddb/api/clientes/${idCliente}`, {
    method: 'DELETE'
  })
    .then(response => response.json())
    .then(data => {
      // Actualizar la tabla
      obtenerClientes();
    })
    .catch(error => {
      console.error('Error al eliminar cliente:', error);
    });
}

// Función para obtener el cliente por ID
function obtenerClientePorID(idCliente) {
  // Realizar una solicitud GET a la API
  return fetch(`http://localhost/contabilidaddb/api/clientes/${idCliente}`, {
    credentials: 'include'
  })
    .then(response => response.json())
    .then(data => data);
}

  
  
    
