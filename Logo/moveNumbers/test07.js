const container = document.getElementById("container");
const characters = ["D", "E", "F", "G"]; // Agrega más caracteres aquí según sea necesario
let currentIndex = 0;

function addCharacter() {
  if (currentIndex < characters.length) {
    const char = document.createElement("span");
    char.className = "moving-char";
    char.textContent = characters[currentIndex];
    container.appendChild(char);
    currentIndex++;
  }
}

// setInterval(addCharacter, 2000); // Agrega un nuevo carácter cada segundo (ajusta el intervalo según tus necesidades)
