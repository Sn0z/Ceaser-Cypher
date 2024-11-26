let slideIndex = 0;
let slideTimeout;

showSlides();

function showSlides() {
  const dots = document.getElementsByClassName("dot");
  const slides = document.getElementsByClassName("background");
  const images = [
    './Images/slide-1.jpg',
    './Images/slide-2.jpg',
    './Images/slide-3.jpg',
    './Images/slide-4.jpg',
  ];

  for (let i = 0; i < slides.length; i++) {
    slides[i].src = `${images[slideIndex]}`;
  }

  for (let i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  dots[slideIndex].className += " active";

  slideIndex = (slideIndex + 1) % images.length;

  clearTimeout(slideTimeout);
  slideTimeout = setTimeout(showSlides, 4000);
}

function currentSlide(index) {
  slideIndex = index;
  showSlides();
}
