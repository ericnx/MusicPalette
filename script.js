window.onload = function () {
  const AUTH_URL = "https://accounts.spotify.com/authorize?client_id=49aeaafc5641456da8fae84026eeb882&response_type=code&redirect_uri=http://localhost:3000&scope=streaming%20user-read-private%20user-library-read%%20user-read-playback";
  const cover = document.getElementById("song-cover");
  cover.src = "afd.jpg";

  // load the song cover
  cover.onload = function () {
    console.log("loaded song cover");
    const ct = new ColorThief(); // ColorThief grabs the color palette of an image
    const numOfColors = 5;
    const palette = ct.getPalette(cover, numOfColors);
    /* palette - clusters similar colors together
                - returns an array containing those colors
                    ex. [[r,g,b], [130,52,23], ...]
                - double array
    */

    for (let i = 0; i < palette.length; i++) {
      const r = palette[i][0];
      const g = palette[i][1];
      const b = palette[i][2];
      const colorSquare = document.getElementById(`color-${i + 1}`);
      colorSquare.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
    }
    const domColor = `${palette[0][0]}, ${palette[0][1]}, ${palette[0][2]}`;
    console.log(`Most dominant color is: RGB(${domColor})`);

    // if song cover fails to load
    cover.onerror = function () {
      alert("error: failed to load image");
    };
  };
};
