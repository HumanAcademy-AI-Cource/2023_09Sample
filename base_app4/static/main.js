function countButton() {
  axios
    .get("http://" + location.hostname + ":8080/counter")
    .then((response) => {
      const counter = document.getElementById("counter");
      counter.innerText = "累計で押された回数：" + response.data.count;
    });
}
