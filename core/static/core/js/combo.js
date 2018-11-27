
$(document).ready(function(){

    $("#cboRegion").change(function() {
        
        var idRegion = $("#cboRegion").val();
        
        if(idRegion=="") {

            $("#cboCiudad").prop("disabled", true);
            $("#itemSeleccionar").prop("selected", true);
            return;
        }

        $.get("formulario.html", {id:idRegion}, function(respuesta){

            //dejamos la respuesta dentro del combobox
            //de comuna
            $("#cboCiudad").html(respuesta);
            $("#cboCiudad").prop("disabled", false);

        });

    });

});
