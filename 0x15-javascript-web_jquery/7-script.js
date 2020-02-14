$(function () {
  let movies = "https://swapi.co/api/people/5/?format=json";
  $.ajax({
    type: 'GET',
    url: movies,
    success: function (people) {
      $('div#character').text(people['name']);
      console.log('Success', people);
    }
  })
});
