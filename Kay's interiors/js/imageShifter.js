const imageContainer1 = document.getElementById('imageContainer1');
const imageContainer2 = document.getElementById('imageContainer2');
const imageContainer3 = document.getElementById('imageContainer3');

const images = [
    './images/home-1.png',
    './images/home-2.png',
    './images/home-3.png'
];

let currentImageIndex1 = 0;
let currentImageIndex2 = 1;
let currentImageIndex3 = 2;

function updateImages() {
    imageContainer1.src = images[currentImageIndex1];
    imageContainer2.src = images[currentImageIndex2];
    imageContainer3.src = images[currentImageIndex3];
}
function shift() {
    // Update image indexes
    currentImageIndex1 = (currentImageIndex1 + 1) % images.length;
    currentImageIndex2 = (currentImageIndex2 + 1) % images.length;
    currentImageIndex3 = (currentImageIndex3 + 1) % images.length;
    
    // Update images
    updateImages();
}