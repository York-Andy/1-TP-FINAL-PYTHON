// Configuración de Vue
const app = Vue.createApp({
    data() {
      return {
        id_cuenta: 0,
        cuenta_acreditada: 0,
        cuenta_debitada: 0,
        descripcion: '',
        id_cliente: 0,
        nombre_cuenta: '',
        numero_cuenta: 0
        // Añade otros campos según sea necesario
      };
    },
    methods: {
      grabarCuentaContable() {
        // Lógica para enviar los datos al servidor
        const datosCuentaContable = {
          id_cuenta: this.id_cuenta,
          cuenta_acreditada: this.cuenta_acreditada,
          cuenta_debitada: this.cuenta_debitada,
          descripcion: this.descripcion,
          id_cliente: this.id_cliente,
          nombre_cuenta: this.nombre_cuenta,
          numero_cuenta: this.numero_cuenta
          // Añade otros campos según sea necesario
        };
  
        // Realiza una petición al servidor para guardar la cuenta contable
        // Puedes utilizar axios u otra librería para manejar peticiones HTTP
         axios.post('/api/cuenta_contable/guardar', datosCuentaContable)
           .then(response => {
        //     // Maneja la respuesta del servidor según sea necesario
           })
           .catch(error => {
        //     // Maneja los errores de la petición
           });
        
        // Muestra un mensaje (puedes personalizar esto según tus necesidades)
        alert('Cuenta Contable grabada exitosamente');
      }
    }
  });
  
  // Monta la aplicación Vue en el contenedor con el ID 'app'
  app.mount('#app');
  