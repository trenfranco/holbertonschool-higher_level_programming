$(function() {
  $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(response) {
    for (let i in response.results) {
      $('UL#list_movies').append('<li>' + response.results[i].title + '</li>');
    }
  });
});
