// Configuración de Vue
const app = Vue.createApp({
    data() {
      return {
        credito: 0,
        debito: 0,
        fecha_registro: '',
        id_cuenta_contable: 0,
        saldo: 0
        // Añade otros campos según sea necesario
      };
    },
    methods: {
      grabarLibroMayor() {
        // Lógica para enviar los datos al servidor
        const datosLibroMayor = {
          credito: this.credito,
          debito: this.debito,
          fecha_registro: this.fecha_registro,
          id_cuenta_contable: this.id_cuenta_contable,
          saldo: this.saldo
          // Añade otros campos según sea necesario
        };
  
        // Realiza una petición al servidor para guardar en el Libro Mayor
        // Puedes utilizar axios u otra librería para manejar peticiones HTTP
         axios.post('/api/libro_mayor/guardar', datosLibroMayor)
           .then(response => {
        //     // Maneja la respuesta del servidor según sea necesario
           })
           .catch(error => {
        //     // Maneja los errores de la petición
           });
        
        // Muestra un mensaje (puedes personalizar esto según tus necesidades)
        alert('Registro en Libro Mayor grabado exitosamente');
      }
    }
  });
  
  // Monta la aplicación Vue en el contenedor con el ID 'app'
  app.mount('#app');
  