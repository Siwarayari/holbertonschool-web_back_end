function handleResponseFromAPI(promise) {
  const pro = promise.then(() => ({ status: 200, body: 'Success' }))
    .catch(() => Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
  return pro;
}
export default handleResponseFromAPI;
