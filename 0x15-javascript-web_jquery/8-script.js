$(function () {
  let movies = "https://swapi.co/api/films/?format=json";
  $.ajax({
    type: 'GET',
    url: movies,
    success: function (films) {
      let filmsDict = films.results;
      for (let sum = 0; sum < filmsDict[sum].film; sum++) {
        console.log('success', filmsDict.results[sum].film);
        $('ul#list_movies').append('<li>' + filmsDict[sum].film + '</li>');
      }
    }
  })
});
