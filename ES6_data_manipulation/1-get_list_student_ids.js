export default function getListStudentIds(arrayobjects) {
  if (!(Array.isArray(arrayobjects))) {
    return [];
  }
  return arrayobjects.map((a) => a.id);
}
