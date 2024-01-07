import {createPushNotificationsJobs} from "./8-job";
import kue from 'kue';
const queue = kue.createQueue();

const mockJobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
];

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});


describe('createPushNotificationsJobs', () => {
    it(`display a error message if jobs is not an array`, () => {
      createPushNotificationsJobs(mockJobs, queue);
      expect(queue.testMode.jobs.type).to.equal(Array);
      });
  });
