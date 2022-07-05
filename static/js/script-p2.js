$(document).ready(function(){

    var ifStyleSubmitted = 0;
    var ifContentSubmitted = 0;

    //$( window ).on( "load", function() {
        $('.style-block').delay(500).animate({'opacity' : 1}, 400, function(){
            $('.content-block').delay(100).animate({'opacity' : 1}, 400, function(){
                $('.back-block').delay(100).animate({'opacity' : 1}, 400);
            })
        });
    //});

        
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

    $('.content-image').click(function(){
        $('#selectcontent').click()  
    })

    $('#submitcontent').on('change', function(event){

        ifContentSubmitted = 1;
        $('.content-image').attr('src', URL.createObjectURL(event.target.files[0]));
    
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

    $("#submitcontent").on('submit', function(e) {
        e.preventDefault()
        var formData = new FormData(this)
        console.log(formData)
        $.ajax({
            url: '/uploadcontent',
            type: 'POST',
            data: formData,
            processData: false, 
            contentType: false,
            success: function(data) {
                $("#contentUUID").text(data.uuid)
            }
        })
    })


    $('#style').click(function(){
        $('#selectstyle').click()  
    })

    $('.style-image').click(function(){
        $('#selectstyle').click()  
    })

    $('#submitstyle').on('change', function(event){

        ifStyleSubmitted = 1;

        $('.style-image').attr('src', URL.createObjectURL(event.target.files[0]));

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

    $("#submitstyle").on('submit', function(e) {
        e.preventDefault()
        var formData = new FormData(this)
        console.log(formData)
        $.ajax({
            url: '/uploadstyle',
            type: 'POST',
            data: formData,
            processData: false, 
            contentType: false,
            success: function(data) {
                console.log(data.uuid)
                $("#styleUUID").text(data.uuid)
            }
        })
    })

    $('#process').click(function(){
        $('.process-block').animate({'opacity' : 0}, 400);
        $('.style-block').delay(0).animate({'opacity' : 0}, 400, function(){
            $('.content-block').delay(100).animate({'opacity' : 0}, 400, function(){
                $('.back-block').delay(100).animate({'opacity' : 0}, 400, function(){

                    var style = $("#styleUUID").text()
                    var content = $("#contentUUID").text()
                    data = {
                        style: style, 
                        content: content
                    }
            
                    $.ajax({
                        url: '/processImage',
                        type: 'POST',
                        contentType: "application/json",
                        data: JSON.stringify(data),
                        success: function(data){
                            window.location.replace("/loadingpage");
                        }
                    })
            

                    
                });
            })
        });
    })

    function ShowProcessBlock(){
        if (ifContentSubmitted == 1 && ifStyleSubmitted == 1){
            $('.process-block').animate({'opacity' : 1}, 400);
        }
    }

})