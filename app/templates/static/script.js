document.addEventListener('DOMContentLoaded', function () {
  // Cargar clientes al cargar la página
  cargarClientes();

  // Evento de envío del formulario para crear o actualizar cliente
  document.getElementById('formulario-cliente').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const clienteData = {};

    formData.forEach((value, key) => {
      clienteData[key] = value;
    });

    // Verificar si se está creando un nuevo cliente o actualizando uno existente
    const clienteId = document.getElementById('btnModificar').dataset.clienteId;

    if (clienteId) {
      // Si hay un clienteId, se está actualizando
      actualizarCliente(clienteId, clienteData);
    } else {
      // Si no hay clienteId, se está creando un nuevo cliente
      crearCliente(clienteData);
    }
  });

  // Evento click en el botón Modificar
  document.getElementById('btnModificar').addEventListener('click', function () {
    const clienteId = this.dataset.clienteId;

    // Cargar datos del cliente en el formulario para modificar
    cargarDatosCliente(clienteId);
  });

  // Evento click en el botón Eliminar
  document.getElementById('btnEliminar').addEventListener('click', function () {
    const clienteId = this.dataset.clienteId;

    // Eliminar cliente
    eliminarCliente(clienteId);
  });
});

// Función para cargar clientes
function cargarClientes() {
  axios.get('http://tu-api.com/clientes')
    .then(function (response) {
      const clientes = response.data;

      // Lógica para mostrar los clientes en la tabla
      // ...

    })
    .catch(function (error) {
      console.error('Error al cargar clientes:', error);
    });
}

// Función para crear un nuevo cliente
function crearCliente(clienteData) {
  axios.post('http://tu-api.com/clientes', clienteData)
    .then(function (response) {
      const nuevoClienteId = response.data.id_cliente;

      // Lógica para actualizar la interfaz con el nuevo cliente
      // ...

      // Limpiar el formulario después de la creación
      document.getElementById('formulario-cliente').reset();
    })
    .catch(function (error) {
      console.error('Error al crear cliente:', error);
    });
}

// Función para cargar datos de un cliente en el formulario para modificar
function cargarDatosCliente(clienteId) {
  axios.get(`http://tu-api.com/clientes/${clienteId}`)
    .then(function (response) {
      const cliente = response.data;

      // Lógica para cargar los datos del cliente en el formulario
      // ...

      // Habilitar el botón de Modificar
      document.getElementById('btnModificar').disabled = false;
      // Establecer el clienteId en el botón Modificar
      document.getElementById('btnModificar').dataset.clienteId = cliente.id_cliente;
      // Habilitar el botón de Eliminar
      document.getElementById('btnEliminar').disabled = false;
      // Establecer el clienteId en el botón Eliminar
      document.getElementById('btnEliminar').dataset.clienteId = cliente.id_cliente;
    })
    .catch(function (error) {
      console.error('Error al cargar datos del cliente:', error);
    });
}

// Función para actualizar un cliente existente
function actualizarCliente(clienteId, clienteData) {
  axios.put(`http://tu-api.com/clientes/${clienteId}`, clienteData)
    .then(function () {
      // Lógica para actualizar la interfaz con los datos actualizados del cliente
      // ...

      // Limpiar el formulario después de la actualización
      document.getElementById('formulario-cliente').reset();

      // Deshabilitar los botones de Modificar y Eliminar
      document.getElementById('btnModificar').disabled = true;
      document.getElementById('btnEliminar').disabled = true;
    })
    .catch(function (error) {
      console.error('Error al actualizar cliente:', error);
    });
}

// Función para eliminar un cliente
function eliminarCliente(clienteId) {
  axios.delete(`http://tu-api.com/clientes/${clienteId}`)
    .then(function () {
      // Lógica para eliminar el cliente de la interfaz
      // ...

      // Limpiar el formulario después de la eliminación
      document.getElementById('formulario-cliente').reset();

      // Deshabilitar los botones de Modificar y Eliminar
      document.getElementById('btnModificar').disabled = true;
      document.getElementById('btnEliminar').disabled = true;
    })
    .catch(function (error) {
      console.error('Error al eliminar cliente:', error);
    });
}




  
  
    
