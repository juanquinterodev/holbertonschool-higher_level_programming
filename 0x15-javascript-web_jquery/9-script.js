$(function () {
  let hello = "https://fourtonfish.com/hellosalut/?lang=fr";
  $.ajax({
    type: 'GET',
    url: hello,
    success: function (names) {
      $('div#hello').text(names['hello']);
      console.log('Success', names);
    }
  })
});
