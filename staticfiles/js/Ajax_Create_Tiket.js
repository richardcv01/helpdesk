

 $(document).ready(function() {
   const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    /* ... */
   ip = 'http://10.44.18.61:80'
   //ip = 'http://localhost:80'


    /* send a POST request to create a todo */
    //$('#form').submit(function(e) {
     $('#send_tiket').click(function(e) {
      e.preventDefault(); // prevent the page from reload
      var url = ip + "/tikets"
      //var data = {
        tikets_PIP = $('#tikets_PIP').val();
        tikets_email = $('#tikets_email').val(),
        tikets_Phone = $('#tikets_Phone').val(),
        tikets_Location = $('#tikets_Location').val(),
        tikets_TopicID = $('#tikets_Topic').val(),
        tikets_Topic = $('#tikets_Topic').find(":selected").text(),
        tikets_text = $('#tikets_text').val(),
        //csrfmiddlewaretoken: csrftoken,
      //}

      $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: url,
        contentType: 'application/json',
        dataType: 'json',
        traditional:true,
        type: 'POST',
        data: JSON.stringify({"tikets":{"tikets_PIP":tikets_PIP, "tikets_email":tikets_email, "tikets_Phone":tikets_Phone,
          "tikets_Location":tikets_Location, "tikets_text": tikets_text,
           "tikets_Topic": {
                "id": tikets_TopicID,
                "topic_text": tikets_Topic
            },
           "tikets_implementation":{
                "id": 1,
                "implementation_text": "Не Виконано"
            },
             "tikets_Owner": {"id":"2", "username": "ALL"}
          }}),
      }).done(function(response) {
           alert('111');
          console.log(data); // let's just print the data in the console for now
        })
          //alert(data["tikets_PIP"]);
      $(this).trigger('reset') // reset the form
    })
  })