$(document).ready(function(){

    var ifStyleSubmitted = 0;
    var ifContentSubmitted = 0;

    $( window ).on( "load", function() {
        $('.style-block').delay(500).animate({'opacity' : 1}, 400, function(){
            $('.content-block').delay(100).animate({'opacity' : 1}, 400, function(){
                $('.back-block').delay(100).animate({'opacity' : 1}, 400);
            })
        });
    });


    $('#back').click(function(){

        $('.button-wrap.back').css(
            {
                'background-position' : '100% 50%',
                'animation': 'none'
            }
        )

        $('.button-back').css(
            {'color' : '#111'}
        )


        $('.process-block').animate({'opacity' : 0}, 400);
        $('.style-block').delay(0).animate({'opacity' : 0}, 400, function(){
            $('.content-block').delay(100).animate({'opacity' : 0}, 400, function(){
                $('.back-block').delay(100).animate({'opacity' : 0}, 400, function(){
                    window.location.replace("/");
                });
            })
        });
    })

    $('#content').click(function(){
        $('#selectcontent').click()  
    })

    $('#submitcontent').on('change', function(){

        ifContentSubmitted = 1;

        $('.button-wrap.content').css(
            {
                'background-position' : '100% 50%',
                'animation': 'none'
            }
        )

        $('.button-content').css(
            {'color' : '#111'}
        )

        console.log(ifContentSubmitted);
        ShowProcessBlock();

        $('#submitcontent').trigger("submit");
        
    })


    $('#style').click(function(){
        $('#selectstyle').click()  
    })

    $('#submitstyle').on('change', function(){

        ifStyleSubmitted = 1;

        $('.button-wrap.style').css(
            {
                'background-position' : '100% 50%',
                'animation': 'none'
            }
        )

        $('.button-style').css(
            {'color' : '#111'}
        )

        $('.button-wrap.style').css({'background-position' : '100% 50%'})

        console.log(ifStyleSubmitted);
        ShowProcessBlock();

        $('#submitstyle').trigger("submit");
        
    })
    // 

    function ShowProcessBlock(){
        if (ifContentSubmitted == 1 && ifStyleSubmitted == 1){
            $('.process-block').animate({'opacity' : 1}, 400);
        }
        
        
    }

})