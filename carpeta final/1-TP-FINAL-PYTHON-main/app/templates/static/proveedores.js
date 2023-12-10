// Configuración de Vue
const app = Vue.createApp({
    data() {
        return {
            proveedores: [],
            url: 'http://mcerda.pythonanywhere.com/proveedores',
            error: false,
            cargando: true,
            // Otros atributos según sea necesario
        };
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.proveedores = data;
                    this.cargando = false;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                });
        },
        // Añade otros métodos según sea necesario
    },
    created() {
        this.fetchData(this.url);
    },
});

// Monta la aplicación Vue en el contenedor con el ID 'app'
app.mount('#app');
