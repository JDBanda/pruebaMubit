$(function () {

    //Definición del elemento SweetAlert
    var Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })

    //Captura del evento submit
    $('#principal_form').submit(function (e) {
        /**
         * Al capturar el evento submit el primer paso a realizar es desactivar el efecto de
         * recarga de la página para realizar las operaciones subsecuentes.
         * 
         * Después se captura el valor de los inputs en variables separadas y se comprueba que
         * la cantidad con la que paga el cliente sea mayor que el monto total, esto activa en la
         * interfaz la clase success o danger y addemás el texto help lo modifica.
         * 
         * Si la condición se cumple se ingresa al método changeAjax()
         */
        e.preventDefault()
        var amount = parseFloat($('#amount').val());
        var client = parseFloat($('#client_change').val());
        if (amount <= client) {
            changeAjax();
            $('#amount').removeClass("is-danger");
            $('#client_change').removeClass("is-danger");
            $('.help').removeClass("is-danger");
            $('#amount').addClass("is-success");
            $('.help').addClass("is-success");
            $('#client_change').addClass("is-success");
            $('.help').text("Si deseas hacer otra venta vuelve a llenar los campos y presiona enter o el botón pagar")
            $('#client_change').toggleClass("is-success");
        } else {
            $('#amount').removeClass("is-success");
            $('#client_change').removeClass("is-success");
            $('.help').removeClass("is-success");
            $('#amount').addClass("is-danger");
            $('.help').addClass("is-danger");
            $('#client_change').addClass("is-danger");
            $('.help').text("Verifique que el monto total de venta no sea mayor al pago del cliente");
        }
    });

    function changeAjax() {
        /**
         * Esta función no recibe parámetros, en primer lugar elimina cualquier elemento dentro del div
         * que contiene las imagenes de billetes y monedas.
         * 
         * Despues se defina la URL y datos que se mandarán al servidor
         * (es muy importante pasar el csrfmiddlewaretoken para usar AJAX)
         * 
         * El último paso será rrecibir la respuesta del servidor, si esta respuesta es buena o mala
         * se define en el servidor y no desde aquí
         * 
         */
        $('#template').empty();
        url = "/caja"
        const data = {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), //Sin esto no se pasan los datos
            amount: $('#amount').val(),
            client_change: $('#client_change').val(),
            cashier: document.getElementById('bienvenida').getAttribute('persona-turno'),
        };
        $.post(url, data, function (response) {
            //Respuesta sobre si guardo o no el monto
            Toast.fire({
                icon: response.content.icon,
                title: response.content.title
            })
            //Mostrar el cambio
            $('#cambio').text(response.content.cambio);
            //Mostrar los billetes en pantalla
            var template = ""
            var obj = JSON.parse(response.content.data)
            for (const key in obj) {
                console.log();
                if (obj[key] > 0) {
                    template += "<p>"
                    for (let index = 0; index < obj[key]; index++) {
                        template += "<img src='static/venta/img/" + key + ".png'> ";
                    }
                    template += "</p>"
                }
            }
            $('#template').append(template)
        });
    }
})