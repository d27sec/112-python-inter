



function init(){
    console.log('init loaded')
    
        //fetch movies details
        //query strings are the random mess after a normal url
    var path = window.location.pathname
    var piece = path.split('/')
    var id= piece[2]
        $.ajax({
            method: 'GET',
            url: '/api/movies/'+id,
            success: function (movie) {
                console.log(movie)
                $('h2').text(movie.title)
            },
            error: function(errorDetails) {
                console.log('error '+ errorDetails)
            }
        })

        
    }


window.onload = init;