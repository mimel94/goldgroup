$(document).ready(function(){
    $('.NavLateral-DropDown').on('click', function(e){
        e.preventDefault();
        var DropMenu=$(this).next('ul');
        var CaretDown=$(this).children('i.NavLateral-CaretDown');
        DropMenu.slideToggle('fast');
        if(CaretDown.hasClass('NavLateral-CaretDownRotate')){
            CaretDown.removeClass('NavLateral-CaretDownRotate');
        }else{
            CaretDown.addClass('NavLateral-CaretDownRotate');
        }

    });
    $('select').material_select();
    $('.datepicker').pickadate({
     selectMonths: true, // Creates a dropdown to control month
     selectYears: 15 // Creates a dropdown of 15 years to control year
    });
    $('.tooltipped').tooltip({delay: 50});
    $('.ShowHideMenu').on('click', function(){
        var MobileMenu=$('.NavLateral');
        if(MobileMenu.css('opacity')==="0"){
            MobileMenu.addClass('Show-menu');
        }else{
            MobileMenu.removeClass('Show-menu');
        }
    });
    $('.btn-ExitSystem').on('click', function(e){
        e.preventDefault();
        swal({
            title: "¿Realmente quieres salir?",
            text: "La seccion actual se cerrara y se saldra del sistema",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Si",
            animation: "slide-from-top",
            closeOnConfirm: false,
            cancelButtonText: "No"
        }, function(){
            window.location='/salir/';
        });
    });
    $('.btn-Search').on('click', function(e){
        e.preventDefault();
        swal({
            title: "What are you looking for?",
            text: "Write what you want",
            type: "input",
            showCancelButton: true,
            closeOnConfirm: false,
            animation: "slide-from-top",
            inputPlaceholder: "Write here",
            confirmButtonText: "Search",
            cancelButtonText: "Cancel"
        }, function(inputValue){
            if (inputValue === false) return false;
            if (inputValue === "") {     swal.showInputError("You must write something");
            return false;
            }
            swal("Nice!", "You wrote: " + inputValue, "success");
        });
    });
    $('.btn-Notification').on('click', function(){
        var NotificationArea=$('.NotificationArea');
        if(NotificationArea.hasClass('NotificationArea-show')){
            NotificationArea.removeClass('NotificationArea-show');
        }else{
            NotificationArea.addClass('NotificationArea-show');
        }
    });
    $('#datos_busqueda ').on('click', function(e){
      var id = e.target.id;
      document.getElementById('id_user').value = id;
      $(".modal-window").slideUp("fast");
      //$("#id_user").text(id);
    });
    $('.search-users').on('click', function(e){
      $(".modal-window").slideDown("slow");
      $.getJSON("/busqueda_asesores/",function( data ){
        var items =[];
        var data_before = $("#datos_busqueda tbody");
        $.each( data['result'], function(key,val){
          items.push("<tr><td id='"+ key +"'>"+ val[0] +"</td><td id='"+ key +"'>"+val[1]+"</td></tr>");
        });
        $("#datos_busqueda").empty("#datos_busqueda tr[1]");
        $(items.join( "" )).appendTo( "#datos_busqueda" );
        //$("<div>").append("se añade un click").appendTo("#datos_busqueda");
      });

      //e.preventDefault();

    });
    $('.close').on('click', function(e){
      $(".modal-window").slideUp("fast");
    });

});
(function($){
    $(window).load(function(){
        $(".NavLateral-content").mCustomScrollbar({
            theme:"light-thin",
            scrollbarPosition: "inside",
            autoHideScrollbar: true,
            scrollButtons:{ enable: true }
        });
        $(".ContentPage, .NotificationArea").mCustomScrollbar({
            theme:"dark-thin",
            scrollbarPosition: "inside",
            autoHideScrollbar: true,
            scrollButtons:{ enable: true }
        });
    });
})(jQuery);
