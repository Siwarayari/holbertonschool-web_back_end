export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const value of map) {
    if (value[1] === 1) {
      map.set(value[0], 100);
    }
  }
  return map;
}
