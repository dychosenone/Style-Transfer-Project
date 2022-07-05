$(document).ready(function(){
    //$( window ).on( "load", function() {

        var data = sessionStorage.getItem('uuid')
        console.log(data)
        $("#refno").text(data)

        $('.sub-text-block').delay(500).animate({'opacity' : '1'})
        $("#head").delay(100).animate({"opacity": "1"}, 400, function(){
            $('.sub-text-block').delay(100).animate({'opacity' : "1"}, 400, function(){
                console.log('a')
                $('.back-block').delay(100).animate({'opacity' : "1"}, 400)
            })
        }); 
    //});

        $('#back').click(function(){
            $('.sub-text-block').delay(100).animate({'opacity' : '0'})
                $("#head").delay(100).animate({"opacity": "0"}, 400, function(){
                    $('.sub-text-block').delay(100).animate({'opacity' : "0"}, 400, function(){
                        $('.back-block').delay(100).animate({'opacity' : "0"}, 400, function(){
                            window.location.replace("/");
                        })
                        
                    })
            }); 
        })



})

/*

                

*/