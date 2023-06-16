function send_data() {
  let name = document.getElementById("name_text").value;
  jQuery.ajax({
    url: '/process_sent_data',
    type: 'POST',
    data: {
      name: name
    }
  });
}
