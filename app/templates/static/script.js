document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.querySelector('.sidebar');
  const main = document.querySelector('main');

  document.querySelector('.navbar-toggler').addEventListener('click', function () {
    sidebar.classList.toggle('show');
    main.classList.toggle('shift');
  });

  const sidebarLinks = document.querySelectorAll('.sidebar a');

  sidebarLinks.forEach(link => {
    link.addEventListener('mouseover', function () {
      this.style.backgroundColor = '#ddd';
      this.style.color = 'black';
    });

    link.addEventListener('mouseout', function () {
      this.style.backgroundColor = '';
      this.style.color = 'white';
    });
  });

  // Cargar clientes al cargar la página
  cargarEntidad('clientes');

  // Evento de envío del formulario para crear o actualizar entidad
  document.getElementById('formulario-entidad').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const entidadData = {};

    formData.forEach((value, key) => {
      entidadData[key] = value;
    });

    // Verificar si se está creando una nueva entidad o actualizando una existente
    const entidadId = document.getElementById('btnModificar').dataset.entidadId;

    if (entidadId) {
      // Si hay un entidadId, se está actualizando
      actualizarEntidad(entidadId, entidadData);
    } else {
      // Si no hay entidadId, se está creando una nueva entidad
      crearEntidad(entidadData);
    }
  });

  // Evento click en el botón Modificar
  document.getElementById('btnModificar').addEventListener('click', function () {
    const entidadId = this.dataset.entidadId;

    // Cargar datos de la entidad en el formulario para modificar
    cargarDatosEntidad(entidadId);
  });

  // Evento click en el botón Eliminar
  document.getElementById('btnEliminar').addEventListener('click', function () {
    const entidadId = this.dataset.entidadId;

    // Eliminar entidad
    eliminarEntidad(entidadId);
  });

});

// Función común para cargar entidades
function cargarEntidad(entidad) {
  axios.get(`http://tu-api.com/${entidad}`)
    .then(function (response) {
      const entidades = response.data;

      // Lógica para mostrar las entidades en la tabla
      // ...

    })
    .catch(function (error) {
      console.error(`Error al cargar ${entidad}:`, error);
    });
}

// Función común para crear una nueva entidad
function crearEntidad(entidadData) {
  axios.post('http://tu-api.com/entidades', entidadData)
    .then(function (response) {
      const nuevaEntidadId = response.data.id_entidad;

      // Lógica para actualizar la interfaz con la nueva entidad
      // ...

      // Limpiar el formulario después de la creación
      document.getElementById('formulario-entidad').reset();

      // Habilitar los botones de Modificar y Eliminar
      document.getElementById('btnModificar').disabled = false;
      document.getElementById('btnEliminar').disabled = false;
    })
    .catch(function (error) {
      console.error(`Error al crear ${entidad}:`, error);
    });
}

// Función común para cargar datos de una entidad en el formulario para modificar
function cargarDatosEntidad(entidadId) {
  axios.get(`http://tu-api.com/entidades/${entidadId}`)
    .then(function (response) {
      const entidad = response.data;

      // Lógica para cargar los datos de la entidad en el formulario
      // ...

      // Habilitar los botones de Modificar y Eliminar
      document.getElementById('btnModificar').disabled = false;
      document.getElementById('btnEliminar').disabled = false;
    })
    .catch(function (error) {
      console.error(`Error al cargar datos de ${entidad}:`, error);
    });
}

// Función común para actualizar una entidad existente
function actualizarEntidad(entidadId, entidadData) {
  axios.put(`http://tu-api.com/entidades/${entidadId}`, entidadData)
    .then(function () {
      // Lógica para actualizar la interfaz con los datos actualizados de la entidad
      // ...

      // Limpiar el formulario después de la actualización
      document.getElementById('formulario-entidad').reset();

      // Deshabilitar los botones de Modificar y Eliminar
      document.getElementById('btnModificar').disabled = true;
      document.getElementById('btnEliminar').disabled = true;
    })
    .catch(function (error) {
      console.error(`Error al actualizar ${entidad}:`, error);
    });
}

// Función común para eliminar una entidad
function eliminarEntidad(entidadId) {
  axios.delete(`http://tu-api.com/entidades/${entidadId}`)
    .then(function () {
      // Lógica para eliminar la entidad de la interfaz
      // ...

      // Limpiar el formulario después de la eliminación
      document.getElementById('formulario-entidad').reset();

      // Deshabilitar los botones de Modificar y Eliminar
      document.getElementById('btnModificar').disabled= false;
      document.getElementById('btnEliminar').disabled = false;
    })
    .catch(function (error) {
      console.error(`Error al eliminar ${entidad}:`, error);
    });
}




  
  
    
