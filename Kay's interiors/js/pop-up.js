function showPopUP() {
        document.querySelector(".pop-up").style.display = "flex";
        document.querySelector(".background").style.filter = "blur(5px)";

}

function closePopUP() {
    document.querySelector(".pop-up").style.display = "none";
    document.querySelector(".background").style.filter = "unset";
}
