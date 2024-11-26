const options1 = document.querySelectorAll('.options-1');
const options2 = document.querySelectorAll('.options-2');

options1.forEach((card, index) => {
    card.addEventListener("click", () => {
      document.querySelector(".main-img-1").style.content = `url(../images/option-1-${index}.png)`;
    });
})

options2.forEach((circle, num) => {
    circle.addEventListener("click", () => {
      document.querySelector(".main-img-2").src = `../images/option-2-${num}.png`;
    });
})
