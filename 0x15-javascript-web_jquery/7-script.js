$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
    console.log(data);
    $('DIV#character').text(data.name);
  });
});
