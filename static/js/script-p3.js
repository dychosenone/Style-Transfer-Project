$(document).ready(function(){
    //$( window ).on( "load", function() {

        var data = sessionStorage.getItem('uuid')
        console.log(data)
        $("#refno").text(data)

        $('.sub-text-block').delay(500).animate({'opacity' : '1'})
        $("#head").delay(500).animate({"opacity": "1"}, 400, function(){
            $('.loading-block').delay(100).animate({'opacity' : "1"}, 400, function(){
                
            })
        }); 
    //});




})

/*

                $('.sub-text-block').delay(500).animate({'opacity' : '0'})
                $("#head").delay(500).animate({"opacity": "0"}, 400, function(){
                    $('.loading-block').delay(100).animate({'opacity' : "0"}, 400, function(){
                        window.location.replace("/resultpage");
                        console.log(data.result)
                    })
                }); 

*/