$(document).ready(function(){
    $("#MascotaFormulario").validate({
        rules: {
            txtNombreMas:{
            required:true,
            minlength: 2,
            maxlength:20,
            
            },
            cboRaza: {
                required: true,
                
            },
            txtGenero: {
                required:true,
                minlength:1,
                maxlength:1,         
            },
            txtFechaIn:{
                required: true,
                date:true,
                
                
            },
            txtFechaNa: {
                date:true,
            },
            cboEstado:{
                required:true
            },
            
            
        },messages:{
            txtNombreMas:{
                required:'Ingrese Nombre'
            },
            cboRaza:{
                required:'Escoja Raza'
            },
            txtGenero:{
                required:'Ingrese Género'
            },
            txtFechaIn:{
                required:'Ingrese Fecha de Ingreso'
            },
            txtFechaNa:{
                required: 'Ingrese Fecha de Nacimiento'
            },
            cboEstado:{
                required:'Escoja Estado'
            }
            
            
        }


    })
});