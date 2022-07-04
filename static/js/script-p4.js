$(document).ready(function(){
    // $( window ).on( "load", function() {

        $('.image-result-block').delay(500).animate({'opacity' : '1'}, 400, function(){
            $(".source-block").delay(100).animate({"opacity": "1"}, 400, function(){
                $('.retry-block').delay(100).animate({'opacity' : "1"}, 400, function(){
                    
                })
            }); 
        })
       
    // });


    $('#retry').click(function(){
        $('.button-wrap.retry').css(
            {
                'background-position' : '100% 50%',
                'animation': 'none'
            }
        )

        $('.button-retry').css(
            {'color' : '#111'}
        )

        $('.image-result-block').delay(100).animate({'opacity' : '0'}, 400, function(){
            $(".source-block").delay(100).animate({"opacity": "0"}, 400, function(){
                $('.retry-block').delay(100).animate({'opacity' : "0"}, 400, function(){
                    window.location.replace("/");
                })
            }); 
        })
       
    })

})