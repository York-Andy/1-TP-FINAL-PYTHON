console.log(location.search); // Lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);
const { createApp } = Vue;
createApp({
    data() {
        return {
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
        grabar() {
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
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow',
            };

            fetch(this.url, options)
                .then(function () {
                    alert("Registro grabado");
                    window.location.href = "./transacciones_contables.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar");
                });
        },
    },
    created() {
        // Lógica para cargar los datos existentes, similar a lo que hiciste en el código anterior
    },
}).mount('#app');
