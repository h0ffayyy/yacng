$(function() {
  $('a#generate').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/generate_codename',
        function(data) {
          $('#codename-text').text(data['codename']).show();
    });
    return false;
  });
});