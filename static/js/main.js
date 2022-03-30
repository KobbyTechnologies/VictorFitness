wow = new WOW({
    boxClass: 'wow', // default
    animateClass: 'animated', // default
    offset: 0, // default
    mobile: true, // default
    live: true // default
})
wow.init();

//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


// var video = document.getElementById("video");

// var timeStarted = -1;
// var timePlayed = 0;
// var duration = 0;
// // If video metadata is laoded get duration
// if (video.readyState > 0)
//     getDuration.call(video);
// //If metadata not loaded, use event to get it
// else {
//     video.addEventListener('loadedmetadata', getDuration);
// }
// // remember time user started the video
// function videoStartedPlaying() {
//     timeStarted = new Date().getTime() / 1000;
// }

// function videoStoppedPlaying(event) {
//     // Start time less then zero means stop event was fired vidout start event
//     if (timeStarted > 0) {
//         var playedFor = new Date().getTime() / 1000 - timeStarted;
//         timeStarted = -1;
//         // add the new ammount of seconds played
//         timePlayed += playedFor;
//     }
//     document.getElementById("played").innerHTML = Math.round(timePlayed) + "";
//     // Count as complete only if end of video was reached
//     if (timePlayed >= duration && event.type == "ended") {
//         document.getElementById("status").className = "complete";
//     }
// }

// function getDuration() {
//     duration = video.duration;
//     document.getElementById("duration").appendChild(new Text(Math.round(
//         duration) + ""));
//     console.log("Duration: ", duration);
// }

// video.addEventListener("play", videoStartedPlaying);
// video.addEventListener("playing", videoStartedPlaying);

// video.addEventListener("ended", videoStoppedPlaying);
// video.addEventListener("pause", videoStoppedPlaying);