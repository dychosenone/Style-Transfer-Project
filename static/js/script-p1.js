$(document).ready(function(){
    //$(window).on('load', function() {
        $("#head").delay(500).animate({"opacity": "1"}, 400, function(){
            $("#body").delay(100).animate({"opacity": "1"}, 400, function(){
                $("#start").delay(100).animate({"opacity": "1"}, 400);
            });
        }); 
    //});

    $("#start_transfer").click(function(){
        $("#start_transfer").css(
            {'color' : '#111'}
        )

        $('.button-wrap').css(
            {
                'background-position' : '100% 50%',
                'animation': 'none'
            }
        )


        $("#head").animate({"opacity": "0"}, 400, function(){
            $("#body").delay(100).animate({"opacity": "0"}, 400, function(){
                $("#start").delay(100).animate({"opacity": "0"}, 400, function(){
                    window.location.replace("/inputpage");
                });
            });
        }); 
    })


})