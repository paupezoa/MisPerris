$(document).ready(function(){
    $("#clienteFormulario").validate({
        rules: {
            txtCorreo:{
            required:true,
            minlength: 5,
            maxlength:40,
            email:true
            },
            txtRut: {
                required: true,
                minlength:9,
                maxlength:10
            },
            txtNombre: {
                required:true,
                minlength:3,
                maxlength:30  ,         
            },
            txtFecha:{
                required: true,
                date:true,
                max:"2001-01-01"
                
            },
            txtFono: {
                required:true,
                min:10000000,
                max:99999999,
                number: true
            },
            cboRegion:{
                required:true
            },
            cboCiudad: {
                required:true
            },
            cboTipoVivienda: {
                required:true
                
            }, 
      
        },messages:{
            txtCorreo:{
                required:'Ingrese correo'
            },
            txtRut:{
                required:'Ingrese rut'
            },
            txtNombre:{
                required:'Ingrese nombre'
            },
            txtFecha:{
                required:'Ingrese Fecha de Nacimiento'
            },
            txtFono:{
                required: 'Ingrese Fono'
            },
            cboCiudad:{
                required:'Escoja una ciudad'
            },
            cboRegion:{
                required:'Escoja una region'
            },
            cboTipoVivienda:{
                required:'Escoja un tipo de Vivienda'
            }
        }


    })
});