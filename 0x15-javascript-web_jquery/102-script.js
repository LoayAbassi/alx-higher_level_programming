$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const translation = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
    $.getJSON(url + translation, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
