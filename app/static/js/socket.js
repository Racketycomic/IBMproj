const socket = io.connect("http://127.0.0.1:5000");
socket.on('connect', function() {
  socket.emit('join_room',{
    username: "{{username}}",
    session_id: "{{session_id}}"
  });

let message_input = document.getElementById('message_input');
document.getElementById('msg_input_form').onsubmit = function(e) {
  e.preventDefault();
  let message = message_input.value.trim();
  if (message.length) {
    socket.emit('send_message', {
      username : "{{username}}",
      session_id : "{{session_id}}",
      message : message
    });
  }
  message_input.value = '';
  message_input.focus();
}
});



    socket.on('recieve_message', function(data) {
      for (key in data){
        if (key == 'user')
        {
          value = data[key]
      const newNode = document.createElement('div');
      newNode.innerHTML = `<b> ${value.username}: &nbsp:</b> ${value.message}`;
      document.getElementById('messages').appendChild(newNode);
    }
      if (key == 'bot_msg') {
        botresp = data[key]
        botresp.forEach( function(item){
        const newNode = document.createElement('div');
        newNode.innerHTML = `<b> watson: &nbsp:</b> ${item}`;
        document.getElementById('messages').appendChild(newNode);
      });
    }
  }

    });
