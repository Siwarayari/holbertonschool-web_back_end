var kue = require('kue');
  
var push_notification_code = kue.createQueue();


function sendNotification(phoneNumber, message){
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

push_notification_code.process('push_notification_code', (job, done) => {
        sendNotification(job.phoneNumber, job.message);
        done();
});
