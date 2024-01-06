import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const arr = [];
  const ClassRoom1 = new ClassRoom(19);
  const ClassRoom2 = new ClassRoom(20);
  const ClassRoom3 = new ClassRoom(34);
  arr.push(ClassRoom1);
  arr.push(ClassRoom2);
  arr.push(ClassRoom3);
  return arr;
}
