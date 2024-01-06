export default function getStudentIdsSum(getListStudents) {
  return getListStudents.reduce((sum, currentValue) => sum + currentValue.id, 0);
}
