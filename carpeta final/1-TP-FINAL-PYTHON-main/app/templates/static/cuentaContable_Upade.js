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
      fetchData(url) {
        fetch(url)
          .then(response => response.json())
          .then(data => {
            console.log(data)
            this.id_cuenta = data.id_cuenta;
            this.cuenta_acreditada = data.cuenta_acreditada;
            this.cuenta_debitada = data.cuenta_debitada;
            this.descripcion = data.descripcion;
            this.id_cliente = data.id_cliente;
            this.nombre_cuenta = data.nombre_cuenta;
            this.numero_cuenta = data.numero_cuenta;
          })
          .catch(err => {
            console.error(err);
            this.error = true;
          });
      },
      modificarCuentaContable() {
        // Lógica para enviar los datos actualizados al servidor
        const datosActualizados = {
          id_cuenta: this.id_cuenta,
          cuenta_acreditada: this.cuenta_acreditada,
          cuenta_debitada: this.cuenta_debitada,
          descripcion: this.descripcion,
          id_cliente: this.id_cliente,
          nombre_cuenta: this.nombre_cuenta,
          numero_cuenta: this.numero_cuenta
          // Añade otros campos según sea necesario
        };
  
        // Realiza una petición al servidor para actualizar la cuenta contable
        // Puedes utilizar axios u otra librería para manejar peticiones HTTP
         axios.post('/api/cuenta_contable/actualizar', datosActualizados)
           .then(response => {
        //     // Maneja la respuesta del servidor según sea necesario
           })
          .catch(error => {
        //     // Maneja los errores de la petición
           });
        
        // Muestra un mensaje (puedes personalizar esto según tus necesidades)
        alert('Cuenta Contable actualizada exitosamente');
      }
    },
    created() {
      this.fetchData(this.url);
    }
  });
  
  // Monta la aplicación Vue en el contenedor con el ID 'app'
  app.mount('#app');
  
