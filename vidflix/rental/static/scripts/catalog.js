function fetchCatalog() {
    // /api/movies
    $.ajax({
        type: 'GET',
        url: '/api/movies',
        success: function (res) {
            console.log(res);
            //the data is in res.objects <= array
            for(let i=0; i<res.objects.length; i++) {
                var movie = res.objects[i];
                displayMovie(movie);
                console.log('ran')
            }
        },
        error: function (errorDetails) {
            console.log('error: ' + errorDetails);
        }
    })
}


function displayMovie(movie) {
  
    var template = 
    `<div class="card" style="width: 18rem;">
    <img style=' height: 350px;' src="${movie.image_url}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">${movie.title}</h5>
      <p class="card-text">${movie.genre.name} - ${movie.length_min} mins </p>
      <label class='card-price'>$ ${movie.price.toFixed(2)}</label>
      <a href="/details/${movie.id}" class="btn btn-primary">Order Now</a>
    </div>
  </div>`

  var container = $('.catalog-container');
  container.append(template);
}

function init() {
    console.log('cat page script');

    fetchCatalog()
}





window.onload = init;