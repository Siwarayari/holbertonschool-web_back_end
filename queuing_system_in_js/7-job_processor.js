var kue = require('kue');
var queue = kue.createQueue();

var blacklisted = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done){
	job.progress(0, 100);
	if (blacklisted.includes(phoneNumber)){
		return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
	}
	else
		job.progress(0, 50);
		console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
		done();
};

queue.process('push_notification_code_2', (job, done) => {
        sendNotification(job.phoneNumber, job.message);
        done();
});
