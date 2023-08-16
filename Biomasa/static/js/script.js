const btnSi = document.getElementById("btnSi");
const btnNo = document.getElementById("btnNo");
const divSi = document.getElementById("divSi");
const divNo = document.getElementById("divNo");

btnSi.addEventListener("click", () => {
  divSi.style.display = "block";
  divNo.style.display = "none";
  btnSi.style.backgroundColor = "green"; // Cambiar el color del botón "Sí"
  btnNo.style.backgroundColor = ""; // Restaurar el color del botón "No"
});

btnNo.addEventListener("click", () => {
  divSi.style.display = "none";
  divNo.style.display = "block";
  btnSi.style.backgroundColor = ""; // Restaurar el color del botón "Sí"
  btnNo.style.backgroundColor = "red"; // Cambiar el color del botón "No"
});