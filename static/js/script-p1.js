$(document).ready(function(){
    $( window ).on( "load", function() {
        $("#head").delay(500).animate({"opacity": "1"}, 400, function(){
            $("#body").delay(100).animate({"opacity": "1"}, 400, function(){
                $("#start").delay(100).animate({"opacity": "1"}, 400);
            });
        }); 
    });

    $("#start_transfer").click(function(){
        $("#head").animate({"opacity": "0"}, 400, function(){
            $("#body").delay(100).animate({"opacity": "0"}, 400, function(){
                $("#start").delay(100).animate({"opacity": "0"}, 400, function(){
                    window.location.replace("/inputpage");
                });
            });
        }); 
    })
})