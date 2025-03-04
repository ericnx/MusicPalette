window.onload = () => {
  checkSong();
  setInterval(checkSong, 1000); // TODO: make it check only when the song changes instead of polling every second
};
function checkSong() {
  fetch("/current_song") // fetches Response object which has the JSON from /current_song
    .then((response) => response.json()) // response is var name, get the JSON from the Response object
    .then((data) => { // then that json is called 'data'
      document.getElementById("cover").src = data.cover;
      document.getElementById("name").innerHTML = data.name;
      document.getElementById("artists").innerHTML = data.artists;
      const palette = document.getElementById("palette");
      palette.innerHTML = "";
      data.palette.forEach((color) => {
        let square = document.createElement("div");
        square.className = "color-squares";
        square.style.backgroundColor = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
        palette.appendChild(square);
      });
    });
}
