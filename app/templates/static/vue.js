import Vue from 'vue';

const app = new Vue({
  el: '#app',
  data: {
    clientes: [],
    cliente: {
      idCliente: '',
      nombre: '',
      razonsocial: '',
      ruc: '',
      direccion: '',
      telefono: '',
      correoelectronico: ''
      // Asegúrate de tener las propiedades necesarias del cliente aquí
    },
  },
  mounted() {
    this.obtenerClientes();
  },
  methods: {
    obtenerClientes() {
      const url = '/clientes';
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.clientes = data;
        })
        .catch(error => {
          console.error('Error al obtener clientes:', error);
        });
    },

    // Método para crear un cliente
    crearCliente() {
      const nombre = this.cliente.nombre;
      const razonsocial = this.cliente.razonsocial;
      const ruc = this.cliente.ruc;
      const direccion = this.cliente.direccion;
      const telefono = this.cliente.telefono;
      const correoelectronico = this.cliente.correoelectronico;

      if (!nombre || nombre.length < 3) {
        alert('El nombre debe tener al menos 3 caracteres.');
        return;
      }

      if (!correoelectronico || !correoelectronico.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)) {
        alert('El correo electrónico no es válido.');
        return;
      }

      const url = '/clientes';
      const datos = {
        nombre,
        razonsocial,
        ruc,
        direccion,
        telefono,
        correoelectronico,
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
          // Agregar el nuevo cliente a la lista
          this.clientes.push(data);

          alert('Cliente creado correctamente.');
          this.limpiarFormulario();
        })
        .catch(error => {
          console.error('Error al crear cliente:', error);
        });
    },

    // Método para actualizar un cliente
    modificarCliente(idCliente) {
      const nombre = this.cliente.nombre;
      const razonsocial = this.cliente.razonsocial;
      const ruc = this.cliente.ruc;
      const direccion = this.cliente.direccion;
      const telefono = this.cliente.telefono;
      const correoelectronico = this.cliente.correoelectronico;

      if (!nombre || nombre.length < 3) {
        alert('El nombre debe tener al menos 3 caracteres.');
        return;
      }

      if (!correoelectronico || !correoelectronico.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)) {
        alert('El correo electrónico no es válido.');
        return;
      }

      const url = `/clientes/${idCliente}`;
      const datos = {
        nombre,
        razonsocial,
        ruc,
        direccion,
        telefono,
        correoelectronico,
      };

      fetch(url, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(datos),
      })
        .then(response => response.json())
        .then(data => {
          // Actualizar la lista de clientes con el cliente modificado
          const index = this.clientes.findIndex(cliente => cliente.id_cliente === idCliente);
          if (index !== -1) {
            this.$set(this.clientes, index, data);
          }

          alert('Cliente modificado correctamente.');
          this.limpiarFormulario();
        })
        .catch(error => {
          console.error('Error al modificar cliente:', error);
        });
    },

    // Método para eliminar un cliente
    eliminarCliente(idCliente) {
      const url = `/clientes/${idCliente}`;

      fetch(url, {
        method: 'DELETE',
      })
        .then(response => {
          if (response.ok) {
            // Eliminar el cliente de la lista
            this.clientes = this.clientes.filter(cliente => cliente.id_cliente !== idCliente);
            alert('Cliente eliminado correctamente.');
            this.limpiarFormulario();
          } else {
            console.error('Error al eliminar cliente:', response.statusText);
          }
        })
        .catch(error => {
          console.error('Error al eliminar cliente:', error);
        });
    },

    // Método para limpiar el formulario después de crear o modificar un cliente
    limpiarFormulario() {
      this.cliente.idCliente = '';
      this.cliente.nombre = '';
      this.cliente.razonsocial = '';
      this.cliente.ruc = '';
      this.cliente.direccion = '';
      this.cliente.telefono = '';
      this.cliente.correoelectronico = '';
    },
  },
});



