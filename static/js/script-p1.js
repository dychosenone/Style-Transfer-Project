$(document).ready(function(){
    //$(window).on('load', function() {
        $("#head").delay(500).animate({"opacity": "1"}, 400, function(){
            $("#body").delay(100).animate({"opacity": "1"}, 400, function(){
                $("#start").delay(100).animate({"opacity": "1"}, 400, function(){
                    $("#input").delay(100).animate({"opacity": "1"}, 400);
                    $(".submit-block").delay(100).animate({"opacity": "1"}, 400);
                });
            });
        }); 
    //});

    $('.input-text').on('input', function(e){
        $(this).css({'width' : ($(this).val().length + 0.5) + 'em'})
    })
     
    $('#submit').click(function(e){
        e.preventDefault()
        if ($('.input-text').val().length == 0){
            alert('Please input your code!')
        }
        else{
            data = $('.input-text').val()
            console.log(data)
            window.location.replace(`/resultpage/${data}`)
        }
    })

    $("#start_transfer").click(function(){
        $("#start_transfer").css(
            {'color' : '#111'}
        )

        $('.button-wrap.start').css(
            {
                'background-position' : '100% 50%',
                'animation': 'none'
            }
        )


        $("#head").animate({"opacity": "0"}, 400, function(){
            $("#body").delay(100).animate({"opacity": "0"}, 400, function(){
                $("#start").delay(100).animate({"opacity": "0"}, 400, function(){
                    $("#input").delay(100).animate({"opacity": "0"}, 400, function(){
                        $(".submit-block").animate({"opacity": "0"}, 400, function(){
                            window.location.replace("/inputpage");
                        });
                    });
                });
            });
        }); 
    })


})