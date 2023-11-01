$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      $('#btn_translate').click();
    }
  });
});
