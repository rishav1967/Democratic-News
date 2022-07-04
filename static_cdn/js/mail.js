
     function sendmail(name,email,message){
      
      var name = $('name').val();
      var email = $('email').val();
      var subject = $('subject').val();
      var message = $('message').val();

      // var body = $('#body').val();

      var Body='Name: '+name+'<br>Email: '+email+' <br>Subject: '+subject+'<br>Message: '+message;
      console.log(name, phone, email, message);

      Email.send({
            Host: "smtp.gmail,com",  
            To: 'wgood814@gmail.com',
            From: "kprahlad007@gmail.com",
            Subject: "New message on contact from "+name,
      }).then(
            message =>{
                  console.log (message);
                  if(message=='OK'){
                  alert('Your mail has been send. Thank you for connecting.');
                  }
                  else{
                        console.error (message);
                        alert('There is error at sending message. ')
                        
                  }

            }
      );



}

