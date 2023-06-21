function clickButton() {
  axios.get("http://" + location.hostname + ":8080/button");
}
