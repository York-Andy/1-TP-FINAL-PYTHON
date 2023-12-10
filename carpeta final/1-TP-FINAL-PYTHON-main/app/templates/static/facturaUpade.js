// Configuración de Vue
const app = Vue.createApp({
    data() {
      return {
        id_factura: 0,
        fecha_emision: '',
        id_clientes: 0,
        impuestos: '',
        numero_factura: 0,
        subtotal: 0,
        total: 0
        // Añade otros campos según sea necesario
      };
    },
    methods: {
      fetchData(url) {
        fetch(url)
          .then(response => response.json())
          .then(data => {
            console.log(data)
            this.id_factura = data.id_factura;
            this.fecha_emision = data.fecha_emision;
            this.id_clientes = data.id_clientes;
            this.impuestos = data.impuestos;
            this.numero_factura = data.numero_factura;
            this.subtotal = data.subtotal;
            this.total = data.total;
          })
          .catch(err => {
            console.error(err);
            this.error = true;
          });
      },
      modificarFactura() {
        // Lógica para enviar los datos actualizados al servidor
        const datosActualizados = {
          id_factura: this.id_factura,
          fecha_emision: this.fecha_emision,
          id_clientes: this.id_clientes,
          impuestos: this.impuestos,
          numero_factura: this.numero_factura,
          subtotal: this.subtotal,
          total: this.total
          // Añade otros campos según sea necesario
        };
  
        // Realiza una petición al servidor para actualizar la factura
        // Puedes utilizar axios u otra librería para manejar peticiones HTTP
         axios.post('/api/factura/actualizar', datosActualizados)
           .then(response => {
        //     // Maneja la respuesta del servidor según sea necesario
          })
          .catch(error => {
        //     // Maneja los errores de la petición
           });
        
        // Muestra un mensaje (puedes personalizar esto según tus necesidades)
        alert('Factura actualizada exitosamente');
      }
    },
    created() {
      this.fetchData(this.url);
    }
  });
  
  // Monta la aplicación Vue en el contenedor con el ID 'app'
  app.mount('#app');
  