
    function ajaxCall() {
        this.send = function(data, url, method, success, type) {
          type = type||'json';
          var successRes = function(data) {
              success(data);
          }

          var errorRes = function(e) {
              console.log(e);
          };
            $.ajax({
                url: url,
                type: method,
                data: data,
                success: successRes,
                error: errorRes,
                dataType: type,
                timeout: 60000
            })

          }

        }

function locationInfo() {
    var call = new ajaxCall();
    this.getCities = function(id) {
        $(".cities option:gt(0)").remove();
        var url = '/cities/?stateId=' + id;
        var method = "get";
        var data = {};
        $('.cities').find("option:eq(0)").html("Por favor espere...");
        call.send(data, url, method, function(data) {
            $('.cities').find("option:eq(0)").html("Seleccione una Ciudad");
            if(data.status == "success"){
                $.each(data['result'], function(key, val) {
                    var option = $('<option />');
                     option.attr('value', key);
                     option.text(val);
                     city = $('#city_Django').val();
                     //alert("ciudad "+city);
                     //alert("llave "+key);
                     if(key == city){
                       option.attr("selected", 'selected');
                     }
                    $('.cities').append(option);
                });
                $(".cities").prop("disabled",false);
            }
        });
    };

    this.getStates = function(id) {
        $(".states option:gt(0)").remove();
        $(".cities option:gt(0)").remove();
        var url = '/states/?countryId=' + id;
        var method = "get";
        var data = {};
        $('.states').find("option:eq(0)").html("Por favor espere...");
        call.send(data, url, method, function(data) {
            $('.states').find("option:eq(0)").html("Seleccione un Estado o Departamento");
            if(data.status == "success"){
                $.each(data['result'], function(key, val) {
                    var option = $('<option />');
                        option.attr('value', val).text(val);
                        option.attr('stateid', key);
                        state = $('#state_Django').val();
                        if(val == state){
                          option.attr("selected", 'selected');
                          var loc = new locationInfo();
                          loc.getCities(key);
                        }
                    $('.states').append(option);
                });
                $(".states").prop("disabled",false);
            }
        });
    };

    this.getCountries = function() {
        var url = '/countries/';
        var method = "get";
        var data = {};
        $('.countries').find("option:eq(0)").html("Por favor espere...");
        call.send(data, url, method, function(data) {
            $('.countries').find("option:eq(0)").html("Seleccione un País");
            if(data.status == "success"){
                $.each(data['result'], function(key, val) {
                    var option = $('<option />');
                    option.attr('value', val).text(val);
                     option.attr('countryid', key);
                     country = $('#country_Django').val();
                     if(val == country){
                       option.attr("selected", 'selected');
                       var loc = new locationInfo();
                       loc.getStates(key);
                     }
                    $('.countries').append(option);

                });
                $(".countries").prop("disabled",false);
            }
        });
    };

}

$(function() {
var loc = new locationInfo();
loc.getCountries();
country = $('#country_Django').val();
$(".countries").on("change", function(ev) {
        var countryId = $("option:selected", this).attr('countryid');
        if(countryId != ''){
        loc.getStates(countryId);
        }
        else{
            $(".states option:gt(0)").remove();
        }
    });
 $(".states").on("change", function(ev) {
        var stateId = $("option:selected", this).attr('stateid');
        if(stateId != ''){
        loc.getCities(stateId);
        }
        else{
            $(".cities option:gt(0)").remove();
        }
    });
});
