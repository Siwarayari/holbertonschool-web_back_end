var kue = require('kue');
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue){
        if (!Array.isArray(jobs))
                throw Error("Jobs is not an array")
        else
                for (const i of jobs) {
                        var job = queue.create('push_notification_code_3', { i }).save( function(err){
                        if( !err ) console.log(`Notification job created: ${job.id}`);
});
job.on('complete', (result) => {
        console.log(`Notification job ${job.id} completed`);})
        .on('failed', (failed) => {
        console.log(`Notification job failed ${failed}`)})
        .on('progress', function(progress, data){
        console.log(`Notification job ${job.id} ${progress} complete`);
})}};
module.exports = createPushNotificationsJobs;
