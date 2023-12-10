// Configuración de Vue
const app = Vue.createApp({
    data() {
        return {
            id_libro_mayor: 0,
            credito: 0,
            debito: 0,
            fecha_registro: '',
            id_cuenta_contable: 0,
            saldo: 0
            // Añade otros campos según sea necesario
        };
    },
    methods: {
        modificarLibroMayor() {
            // Lógica para enviar los datos al servidor
            const datosLibroMayor = {
                id_libro_mayor: this.id_libro_mayor,
                credito: this.credito,
                debito: this.debito,
                fecha_registro: this.fecha_registro,
                id_cuenta_contable: this.id_cuenta_contable,
                saldo: this.saldo
                // Añade otros campos según sea necesario
            };

            // Realiza una petición al servidor para modificar el Libro Mayor
            // Puedes utilizar axios u otra librería para manejar peticiones HTTP
             axios.put(`/api/libro_mayor/${this.id_libro_mayor}`, datosLibroMayor)
               .then(response => {
            //     // Maneja la respuesta del servidor según sea necesario
               })
               .catch(error => {
            //     // Maneja los errores de la petición
               });

            // Muestra un mensaje (puedes personalizar esto según tus necesidades)
            alert('Registro en Libro Mayor modificado exitosamente');
        }
    }
});

// Monta la aplicación Vue en el contenedor con el ID 'app'
app.mount('#app');
