$(document).ready(function(){
    $( window ).on( "load", function() {
        $("#head").delay(500).animate({"opacity": "1"}, 400, function(){
            $("#body").delay(150).animate({"opacity": "1"}, 400, function(){
                $("#start").delay(150).animate({"opacity": "1"}, 400);
            });
        }); 
    });

    $("#start_transfer").click(function(){
        $("#head").delay(150).animate({"opacity": "0"}, 400, function(){
            $("#body").delay(150).animate({"opacity": "0"}, 400, function(){
                $("#start").delay(150).animate({"opacity": "0"}, 400, function(){
                    window.location.replace("/inputpage");
                });
            });
        }); 
    })
})