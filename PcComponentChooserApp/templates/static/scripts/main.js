function fadeOut(element) {
    let op = 1;
    let timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
            element.remove();
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 50);
}

window.onload = function() {
    alerts = document.querySelectorAll(".alert");
    for (let i = 1; i <= alerts.length; i++) {
        window.setTimeout(function() {
            fadeOut(alerts[i-1]);
        },
        5000*i);
    }
};