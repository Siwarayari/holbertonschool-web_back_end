import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('ready', () => {
    console.log('Redis client connected to the server');
  });

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

function setNewSchool(schoolName, value){
	client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName){
	await client.get(schoolName, (err, name) => {
   		console.log(name);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
