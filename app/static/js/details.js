// Show the detail of the event indicated
// By default the details of all events on the map are hidden
function showDetails(type, index) {
    let eventID = type+index;
    let events = document.getElementById("details").getElementsByTagName("div");

    // Hide every event details
    for(var i=0; i<events.length; i++) {
             events[i].style.display = "none";
    }
    // Show the details of the correct event
    document.getElementById(eventID).style.display = "contents";
}