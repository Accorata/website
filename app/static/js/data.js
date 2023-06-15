function send_data(name) {
  console.log("aaaa");
  jQuery.ajax({
    url: '/process_sent_data',
    type: 'POST',
    data: {
      name: name
    }
  });
}
