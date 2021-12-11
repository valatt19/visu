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


// Slides code for showing erruptions of a volcano(from w3school)
slideIndex = 1

function plusSlides(n,j) {
  showSlides(slideIndex += n,j);
}

function currentSlide(n,j) {
  showSlides(slideIndex = n);
}

function showSlides(n,j) {
  var i;
  var v = "mySlides"+j
  var slides = document.getElementsByClassName(v);
  //var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  //for (i = 0; i < dots.length; i++) {
  //    dots[i].className = dots[i].className.replace(" active", "");
  //}
  slides[slideIndex-1].style.display = "block";  
  //dots[slideIndex-1].className += " active";
}