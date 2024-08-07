$(document).ready(() => {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    const movies = data.results;
    for (let movie = 0; movie < movies.length; movie++) {
      $('UL#list_movies').append('<li>' + movies[movie].title + '</li>');
    }
    console.log(movies);
  });
});
