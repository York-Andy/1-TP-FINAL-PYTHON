// Configuración de Vue
const app = Vue.createApp({
    data() {
        return {
            nombre: "",
            correo: "",
            direccion: "",
            ruc: 0,
            telefono: 0,
            url: 'http://mcerda.pythonanywhere.com/proveedores',
            // Otros atributos según sea necesario
        };
    },
    methods: {
        grabar() {
            let proveedor = {
                nombre: this.nombre,
                correo_electronico: this.correo,
                direccion: this.direccion,
                ruc: this.ruc,
                telefono: this.telefono
            };

            var options = {
                body: JSON.stringify(proveedor),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };

            fetch(this.url, options)
                .then(function () {
                    alert("Proveedor grabado");
                    window.location.href = "./proveedores.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar");
                });
        },
        // Añade otros métodos según sea necesario
    },
});

// Monta la aplicación Vue en el contenedor con el ID 'app'
app.mount('#app');
