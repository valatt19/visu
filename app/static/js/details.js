// Show the detail of the event indicated
// By default the details of all events on the map are hidden
function showDetails(type, index) {
    let eventID = type+index;
    let events = document.getElementsByClassName("details_table");

    // Hide every event details
    for(var i=0; i<events.length; i++) {
             events[i].style.display = "none";
    }
    // Show the details of the correct event
    document.getElementById(eventID).style.display = "contents";
}

//W3SCHOOL
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}