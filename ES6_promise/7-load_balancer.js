export default function loadBalancer(chinaDownload, USDownload) {
  const racepromise = Promise.race([chinaDownload, USDownload]);
  return racepromise;
}
