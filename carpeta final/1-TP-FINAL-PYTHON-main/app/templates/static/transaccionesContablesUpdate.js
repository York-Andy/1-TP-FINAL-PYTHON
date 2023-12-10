console.log(location.search); // Lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);
const { createApp } = Vue;
createApp({
    data() {
        return {
            id: 0,
            cuentaAcreditada: 0,
            cuentaDebitada: 0,
            descripcion: "",
            fechaTransaccion: "",
            monto: 0,
            tipoTransaccion: "",
            url: 'http://mcerda.pythonanywhere.com/transacciones_contables/' + id,
        };
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id = data.id
                    this.cuentaAcreditada = data.cuenta_acreditada;
                    this.cuentaDebitada = data.cuenta_debitada;
                    this.descripcion = data.descripcion;
                    this.fechaTransaccion = data.fecha_transaccion;
                    this.monto = data.monto;
                    this.tipoTransaccion = data.tipo_transaccion;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                });
        },
        modificar() {
            let transaccionContable = {
                cuenta_acreditada: this.cuentaAcreditada,
                cuenta_debitada: this.cuentaDebitada,
                descripcion: this.descripcion,
                fecha_transaccion: this.fechaTransaccion,
                monto: this.monto,
                tipo_transaccion: this.tipoTransaccion,
            };
            var options = {
                body: JSON.stringify(transaccionContable),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };
            fetch(this.url, options)
                .then(function () {
                    alert("Registro modificado");
                    window.location.href = "./transacciones_contables.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar");
                });
        },
    },
    created() {
        this.fetchData(this.url);
    },
}).mount('#app');
