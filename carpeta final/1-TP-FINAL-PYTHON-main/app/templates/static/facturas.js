const { createApp } = Vue;
createApp({
  data() {
    return {
      facturas: [],
      url: 'http://mcerda.pythonanywhere.com/facturas',
      error: false,
      cargando: true,
      // Añade otros campos según sea necesario
      fecha_emision: "",
      id_clientes: 0,
      id_factura: 0,
      impuestos: "",
      numero_factura: 0,
      subtotal: 0,
      total: 0,
    };
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.facturas = data;
          this.cargando = false;
        })
        .catch(err => {
          console.error(err);
          this.error = true;
        });
    },
    eliminar(factura) {
      const url = this.url + '/' + factura;
      var options = {
        method: 'DELETE',
      };
      fetch(url, options)
        .then(res => res.text()) // or res.json()
        .then(res => {
          location.reload();
        });
    },
    grabar() {
      let factura = {
        fecha_emision: this.fecha_emision,
        id_clientes: this.id_clientes,
        id_factura: this.id_factura,
        impuestos: this.impuestos,
        numero_factura: this.numero_factura,
        subtotal: this.subtotal,
        total: this.total,
        // Añade otros campos según sea necesario
      };
      var options = {
        body: JSON.stringify(factura),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow',
      };
      fetch(this.url, options)
        .then(function () {
          alert("Registro grabado");
          window.location.href = "./facturas.html";
        })
        .catch(err => {
          console.error(err);
          alert("Error al Grabar");
        });
    },
  },
  created() {
    this.fetchData(this.url);
  },
}).mount('#app');
