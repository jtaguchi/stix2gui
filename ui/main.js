/* global $, eel */
$(document).ready(function() {
  eel.expose(set_output_text);
  function set_output_text(text) {
    $('#outputText').val(text);
  }

  function load_stix_string(input_text) {
    eel.load_stix_string(input_text)();
  }

  function parse_text() {
    load_stix_string($('#inputText').val());
  }

  $('#parseButton').on('click', parse_text);
});
