console.log(location.search); // Lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);

const { createApp } = Vue;
createApp({
  data() {
    return {
      id: 0,
      nombre: "",
      correo_electronico: "",
      direccion: "",
      razon_social: "",
      ruc: 0,
      telefono: 0,
      url: 'http://localhost/clientes/' + id,
    };
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.id = data.id_cliente;
          this.nombre = data.nombre;
          this.correo_electronico = data.correo_electronico;
          this.direccion = data.direccion;
          this.razon_social = data.razon_social;
          this.ruc = data.ruc;
          this.telefono = data.telefono;
        })
        .catch((err) => {
          console.error(err);
          this.error = true;
        });
    },
    modificar() {
      let cliente = {
        nombre: this.nombre,
        correo_electronico: this.correo_electronico,
        direccion: this.direccion,
        razon_social: this.razon_social,
        ruc: this.ruc,
        telefono: this.telefono,
      };

      var options = {
        body: JSON.stringify(cliente),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow',
      };

      fetch(this.url, options)
        .then(function () {
          alert("Registro modificado");
          window.location.href = "./clientes.html";
        })
        .catch((err) => {
          console.error(err);
          alert("Error al Modificar");
        });
    },
  },
  created() {
    this.fetchData(this.url);
  },
}).mount('#app');
