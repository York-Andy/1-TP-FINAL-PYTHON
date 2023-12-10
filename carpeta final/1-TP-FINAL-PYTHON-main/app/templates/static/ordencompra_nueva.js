// Configuración de Vue
const app = Vue.createApp({
    data() {
        return {
            id_orden_compra: 0,
            fecha_emision: '',
            id_clientes: 0,
            id_proveedores: 0,
            impuestos: 0,
            numero_orden: 0,
            subtotal: 0,
            total: 0
            // Añade otros campos según sea necesario
        };
    },
    methods: {
        grabarOrdenCompra() {
            // Lógica para enviar los datos al servidor
            const datosOrdenCompra = {
                id_orden_compra: this.id_orden_compra,
                fecha_emision: this.fecha_emision,
                id_clientes: this.id_clientes,
                id_proveedores: this.id_proveedores,
                impuestos: this.impuestos,
                numero_orden: this.numero_orden,
                subtotal: this.subtotal,
                total: this.total
                // Añade otros campos según sea necesario
            };

            // Realiza una petición al servidor para grabar la Orden de Compra
            // Puedes utilizar axios u otra librería para manejar peticiones HTTP
             axios.post('/api/orden_compra', datosOrdenCompra)
               .then(response => {
            //     // Maneja la respuesta del servidor según sea necesario
               })
               .catch(error => {
            //     // Maneja los errores de la petición
               });

            // Muestra un mensaje (puedes personalizar esto según tus necesidades)
            alert('Orden de Compra grabada exitosamente');
        }
    }
});

// Monta la aplicación Vue en el contenedor con el ID 'app'
app.mount('#app');
