var i = 0;
var txt = 'Ну а кто не хочет права? Сдай быстро, как твоя будущая машина и также легко, как думать о том, что она не ломается! '; /* Текст */
var speed = 50; /* Скорость/длительность эффекта в миллисекундах */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("enter").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}