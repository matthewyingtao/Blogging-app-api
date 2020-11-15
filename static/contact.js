// Select the button
const business = document.querySelector('#business');
const personal = document.querySelector('#personal');
var mode = false;

// Listen for a click on the button
business.addEventListener('click', function() {
    $("#form-use").html("Business");
    $(".form-container").css("max-height", "1000vh");
    $(".form-container").css("min-height", "fit-content");
    $(".form-container").css("padding", "15px");
    $("#hero").css("min-height", "40vh");
})

// Listen for a click on the button
personal.addEventListener('click', function() {
    $("#form-use").html("Personal");
    $(".form-container").css("max-height", "150vh");
    $(".form-container").css("min-height", "fit-content");
    $(".form-container").css("padding", "15px");
    $("#hero").css("min-height", "40vh");
})