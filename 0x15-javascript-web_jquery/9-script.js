$( document ).ready(function() {
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(response) {
    $('#hello').text(response.hello);
  });
});
