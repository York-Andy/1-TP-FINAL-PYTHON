import Vue from 'vue';

// Importar el código de Vue.js
import './vue.js';

const app = new Vue({
  el: '#app',
  data: {
    clientes: [],
    cliente: {
      nombre: '',
      correo: '',
      idClientes: '',
    },
  },
  mounted() {
    this.obtenerClientes();
  },
  methods: {
    obtenerClientes() {
      // Enviar la solicitud GET a la API
      const url = '/clientes';
      fetch(url)
        .then(response => response.json())
        .then(data => {
          // Actualizar la lista de clientes
          this.clientes = data;
        })
        .catch(error => {
          console.error('Error al obtener clientes:', error);
        });
    },
    crearCliente() {
      // Obtener los datos del cliente del formulario
      const nombre = this.cliente.nombre;
      const correo = this.cliente.correo;

      // Validar datos del usuario
      if (!nombre || nombre.length < 3) {
        alert('El nombre debe tener al menos 3 caracteres.');
        return;
      }

      if (!correo || !correo.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)) {
        alert('El correo electrónico no es válido.');
        return;
      }

      // Enviar la solicitud POST a la API
      const url = '/clientes';
      const datos = {
        nombre,
        correo,
      };

      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(datos),
      })
        .then(response => response.json())
        .then(data => {
          // Actualizar la lista de clientes
          this.clientes.push(data);

          // Mostrar un mensaje de confirmación
          alert('Cliente creado correctamente.');

          // Limpiar los datos del formulario
          this.cliente.nombre = '';
          this.cliente.correo = '';
        })
        .catch(error => {
          console.error('Error al crear cliente:', error);
        });
    },
  },
});

