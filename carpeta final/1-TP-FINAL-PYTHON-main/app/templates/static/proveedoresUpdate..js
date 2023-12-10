console.log(location.search); // Lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);
const { createApp } = Vue;
createApp({
    data() {
        return {
            id: 0,
            nombre: "",
            correo: "",
            direccion: "",
            ruc: 0,
            telefono: 0,
            // Otros atributos según sea necesario
        };
    },
    methods: {
        fetchData(url) {
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.id = data.id;
                this.nombre = data.nombre;
                this.correo = data.correo;
                this.direccion = data.direccion;
                this.ruc = data.ruc;
                this.telefono = data.telefono;
            })
            .catch(err => {
                console.error(err);
                this.error = true;
            });
        },
        modificar() {
            let proveedor = {
                nombre: this.nombre,
                correo: this.correo,
                direccion: this.direccion,
                ruc: this.ruc,
                telefono: this.telefono,
                // Agrega otros campos según sea necesario
            };
            var options = {
                body: JSON.stringify(proveedor),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };
            fetch(this.url, options)
            .then(function () {
                alert("Registro modificado");
                window.location.href = "./proveedores.html";
            })
            .catch(err => {
                console.error(err);
                alert("Error al Modificar");
            });
        }
    },
    created() {
        this.fetchData(this.url);
    },
}).mount('#app');
