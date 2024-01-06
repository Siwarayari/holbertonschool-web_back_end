export default function getListStudentIds(arrayobjects, city) {
  if (!(Array.isArray(arrayobjects))) {
    return [];
  }
  return arrayobjects.filter((arrayobjects) => arrayobjects.location === city);
}
