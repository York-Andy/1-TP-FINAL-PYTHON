// Función para realizar una solicitud GET a la API para obtener clientes
function obtenerClientes() {
    fetch('/clientes', {
      credentials: 'include'
    })
      .then(response => response.json())
      .then(data => {
        document.getElementById('resultadoClientes').innerHTML = `
          <table class="table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Correo electrónico</th>
              </tr>
            </thead>
            <tbody>
              ${data.map(cliente => `
                <tr>
                  <td>${cliente.id}</td>
                  <td>${cliente.nombre}</td>
                  <td>${cliente.correo_electronico}</td>
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
  
  // Función para realizar una solicitud POST a la API para crear un nuevo cliente
  function crearCliente() {
    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
  
    // Validar datos del usuario
    if (!nombre || nombre.length < 3) {
      alert('El nombre debe tener al menos 3 caracteres.');
      return;
    }
  
    if (!correo || !correo.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)) {
      alert('El correo electrónico no es válido.');
      return;
    }
  
    fetch('/clientes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        nombre: nombre,
        correo_electronico: correo
        // Agrega otros campos según la estructura de tu API
      })
    })
      .then(response => response.json())
      .then(data => {
        document.getElementById('resultadoCrearCliente').innerHTML = `
          <div class="alert alert-success">
            Cliente creado correctamente.
          </div>
        `;
      })
      .catch(error => {
        console.error('Error al crear cliente:', error);
      });
  
    // Evitar que el formulario envíe una solicitud tradicional
    return false;
  }
  
    
