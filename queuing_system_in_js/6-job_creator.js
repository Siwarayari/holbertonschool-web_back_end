var kue = require('kue');

var push_notification_code = kue.createQueue();


const jobdata = {
  phoneNumber: "string",
  message: "string",
};

var job = push_notification_code.create('email', { jobdata }).save( function(err){
   if( !err ) console.log(`Notification job created: ${job.id}`);
});


job.on('complete', (result) => {
    console.log('Notification job completed');
  }).on('failed', (failed) => {
  console.log('Notification job failed')});
