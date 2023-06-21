const takePhoto = () => {
  axios.get("http://" + location.hostname + ":8080/shot").then((response) => {
    const photo_image = document.getElementById("photo-image");
    photo_image.src = response.data.photo_name;
  });
};
