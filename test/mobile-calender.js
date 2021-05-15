let calender = document.getElementById('sidebar');
let showing = false;
function toggle (toggle) {
    if (showing) {
        calender.style.transition = "1s"
        calender.style.display = "inline";
        showing = !showing;
    }
    else {
        calender.style.display = "none";
        showing = !showing;
    }
};