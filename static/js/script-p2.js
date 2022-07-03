$(document).ready(function(){
    $( window ).on( "load", function() {
        $('.style-block').delay(500).animate({'opacity' : 1}, 400, function(){
            $('.content-block').delay(100).animate({'opacity' : 1}, 400, function(){
                $('.back-block').delay(100).animate({'opacity' : 1}, 400);
            })
        });
    });


    $('#back').click(function(){
        $('.style-block').delay(0).animate({'opacity' : 0}, 400, function(){
            $('.content-block').delay(100).animate({'opacity' : 0}, 400, function(){
                $('.back-block').delay(100).animate({'opacity' : 0}, 400, function(){
                    window.location.replace("/");
                });
            })
        });
    })
   
})