

    $(document).ready(function () {
        var arrayImplem = new Map();
        var arrayUsers = new Map();
        inplemention_data = "";
        tikets_implementation_id = "";
        tikets_Owner = new Map();
        idslect = "";
        button = "";
        ip = 'http://10.44.18.61:80'
        //ip = 'http://localhost:80'

        function getInplemention() {
                        //var arrayImplem = new Map();
                         $.ajax({
                         type: "GET",
                         async: true,
                         //url: 'http://127.0.0.1:80/inplemention',
                         url: ip + '/inplemention',
                         data: "",
                           success: function(data) {
                            data = data['implementation_text'];
                            inplemention_data = data;
                            Object.keys(data).forEach(key => {
                               arrayImplem.set(inplemention_data[key].id, inplemention_data[key].implementation_text);
                            });
                         }
                                  });
                           return false;  }

          function getUsers() {
                        //var arrayImplem = new Map();
                         $.ajax({
                         type: "GET",
                         async: true,
                         //url: 'http://127.0.0.1:80/users',
                         url: ip + '/users',
                             data: "",
                           success: function(data) {
                            data = data['username'];
                            users_data = data;
                            Object.keys(data).forEach(key => {
                               arrayUsers.set(users_data[key].id, users_data[key].username);
                            });

                         }
                                  });
                           return false;  }

               function getTiket(id) {
                     //alert('get'+  id)
                     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                     $.ajax({
                        type: 'GET',
                       async: true,
                       //url: 'http://127.0.0.1:80/tikets/'+id,
                       url: ip + '/tikets/'+id,
                         data: "",
                         success: function(data) {
                 data = data['tikets'];
                 data = data.tikets_implementation.id
                 //data = inplemention_data;
                 //alert('data'+ data);
                 tikets_implementation_id = data;
                 //alert('tikets_implementation_id get'+tikets_implementation_id)
                 }
               });
              return false;
              //return data;
                  }

              function getUser_send_ajax() {
                     //alert('get'+  id)
                     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                     $.ajax({
                        type: 'GET',
                       async: true,
                       //url: 'http://127.0.0.1:80/tikets/'+id,
                       url: ip + '/send_user_ajax/',
                         data: "",
                         success: function(data) {
                 data = data;
                 //alert(data['username']);
                 //alert(data['id']);
                 tikets_Owner['id'] = data['id'];
                 tikets_Owner['username'] = data['username'];
                 //alert(tikets_Owner['username'])
                 }
               });
              return false;
              //return data;
                  }



               function putTiket(id, dataupdate, user) {
                     //getUser_send_ajax();
                     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                       switch(tikets_implementation_id){
                       case 1:
                           tikets_implementation_id = tikets_implementation_id+1;
                           //button = 'button1';
                           break;
                       case 2:
                           tikets_implementation_id = tikets_implementation_id+1;
                           //button = 'button2';
                           break;
                       case 3:
                           tikets_implementation_id = 1;
                           //button = 'button3';
                           break;
                       }

                     $.ajax({
                       headers: {'X-CSRFToken': csrftoken},
                       type: 'PUT',
                       //async: true,
                       contentType: 'application/json',
                       dataType: 'json',
                       traditional:true,
                       //url: 'http://127.0.0.1:80/tikets/'+id+'/' ,
                         //alert(arrayImplem),
                       url: ip + '/tikets/'+id+'/' ,
                         data: JSON.stringify( {"pk":id, "tikets_implementation":{"id":tikets_implementation_id, "implementation_text":"1"},
                                                                       "tikets_Owner": {"id":tikets_Owner.id, "username": tikets_Owner.username}}),
             success: function(data) {
                 data = inplemention_data;

                 }
               });
                   //update(id);
                   updatetr(dataupdate);
              return false;  }

              function updatetr(data) {
                      //alert(idslect)
                      //alert(tikets_implementation_id)
                      //alert(idslect);

                           switch(tikets_implementation_id){
                       case 1:
                           //tikets_implementation_id = tikets_implementation_id+1;
                           button = 'button1';
                           break;
                       case 2:
                           //tikets_implementation_id = tikets_implementation_id+1;
                           button = 'button2';
                           break;
                       case 3:
                           //tikets_implementation_id = 1;
                           button = 'button3';
                           break;                 }
                           //alert(arrayImplem.get(tikets_implementation_id));
                            $("tr#"+idslect).empty();
                            $("#table > tbody > tr#"+idslect).append(//"<tr>" +
                            "<td>" + data.pk + "</td>" +
                            "<td>" + data.tikets_PIP + "</td>" +
                            "<td>" + data.tikets_email + "</td>" +
                            "<td>" + data.tikets_Phone + "</td>" +
                            "<td>" + data.tikets_Location + "</td>" +
                            "<td>" + data.tikets_Topic.topic_text + "</td>" +
                            "<td>" + data.tikets_text + "</td>" +
                            "<td>" + data.tikets_Owner.username + "</td>" +
                            //"<td>" + '<a class="button" href='+ this.url+"/"+data[key].pk+' >'+data[key].tikets_implementation.implementation_text + "</a>" + "</td>" +
                            "<td>"
                                + '<a id="'+data.pk + '" class="'+button+'" href="" >'+arrayImplem.get(tikets_implementation_id) + "</a>" +
                                //+ '<a id="'+data.pk + '" class=button2" href="" >'+data.tikets_implementation.implementation_text + "</a>" +
                             "</td>"
                                //+
                            //"</tr>"
                            );

              }

              function update(id) {
                       $.ajax({
                       type: 'GET',
                       async: true,
                       //url: 'http://127.0.0.1:80/tikets/'+id,
                       url: ip + '/tikets/'+id,
                           data: "",
                       success: function (data) {
                            //$("tbody").empty();
                          data = data['tikets'];
                          idslect = data.pk;
                          tikets_implementation_id = data.tikets_implementation.id;
                          //tikets_Owner = data.tikets_Owner.id;
                          putTiket(id, data, "r.chagley");
                          updatetr(data);
                       }
                   });
              }

         $('#table').on('click','a',function() {
                   //getInplemention();
                   var id = $(this).attr('id');
                   //getTiket(id);
                   //putTiket(id);
                     update(id);
               return false;
        });


        $("#ajax-text-me").click(function() {
            getInplemention();
            getUser_send_ajax();
            //getUsers();
            //alert()
            $.ajax({
                type: 'GET',
                async: true,
                //url: 'http://127.0.0.1:8000/tikets',
                url: ip + '/tikets',
                data: "",
                success: function(data) {
                    data = data['tikets'];
                    $('tbody').empty();
                    Object.keys(data).forEach(key => {
                        button = "";
                        //alert(data[key].tikets_implementation.id)
                        if (data[key].tikets_implementation.id == 1)
                           {
                              button = "button1";
                           }else if (data[key].tikets_implementation.id == 2)
                           {
                               button = "button2";
                           }else if (data[key].tikets_implementation.id == 3)
                               button = "button3";
                        $("#table > tbody").append("<tr id="+data[key].pk+">" +
                            "<td>" + data[key].pk + "</td>" +
                            "<td>" + data[key].tikets_PIP + "</td>" +
                            "<td>" + data[key].tikets_email + "</td>" +
                            "<td>" + data[key].tikets_Phone + "</td>" +
                            "<td>" + data[key].tikets_Location + "</td>" +
                            "<td>" + data[key].tikets_Topic.topic_text + "</td>" +
                            "<td>" + data[key].tikets_text + "</td>" +
                            "<td>" + data[key].tikets_Owner.username + "</td>" +
                            //"<td>" + '<a class="button" href='+ this.url+"/"+data[key].pk+' >'+data[key].tikets_implementation.implementation_text + "</a>" + "</td>" +
                            " <td>" + '<a id="'+data[key].pk+ '" class="'+button+'" href="" >'+data[key].tikets_implementation.implementation_text + "</a>" + "</td>" +
                            //" <td>" + '<a id="'+data[key].pk+ '" class="button1" href="" >'+data[key].tikets_implementation.implementation_text + "</a>" + "</td>" +
                            "</tr>");

                    });

                },
                dataType: 'json',
            });
        });
    });

