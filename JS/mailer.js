var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  host: 'mail.tobias-weiss.org',
  port: 25,
  auth: {
    user: 'user@domain.de',
    pass: 'password'
  }
});

var mailOptions = {
  from: 'beacon@smt.de',
  to: 'tobias@tobias-weiss.org',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
}); 
