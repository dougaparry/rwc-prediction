
function showPrediction(game, prob1, prob2, teamA, teamB){
  document.getElementById(game+"-1").className = "text-center";
  document.getElementById(game+"-2").className = "text-center";
  document.getElementById(game+"-3").className = "text-center";

  if (prob1 > prob2){
    document.getElementById(game+teamA).style.color = "green";
  } else {
    document.getElementById(game+teamB).style.color = "green";
  }
}


// Function to determine which game to scroll to
// compares the current date to any of the upcoming ones,
// scrolling to the next most likely game

function determine(){
  var currentTime = new Date();
  var games = [];

  var game1 = new Date('September 18, 2015 21:00:00');
  games.push(game1);
  var game2 = new Date('September 19, 2015 13:00:00');
  games.push(game2);
  var game3 = new Date('September 19, 2015 15:30:00');
  games.push(game3);
  var game4 = new Date('September 19, 2015 17:45:00');
  games.push(game4);
  var game5 = new Date('September 19, 2015 21:00:00');
  games.push(game5);
  var game6 = new Date('September 20, 2015 13:00:00');
  games.push(game6);
  var game7 = new Date('September 20, 2015 15:30:00');
  games.push(game7);
  var game8 = new Date('September 20, 2015 17:45:00');
  games.push(game8);
  var game9 = new Date('September 23, 2015 15:30:00');
  games.push(game9);
  var game10 = new Date('September 23, 2015 17:45:00');
  games.push(game10);
  var game11 = new Date('September 23, 2015 21:00:00');
  games.push(game11);
  var game12 = new Date('September 24, 2015 21:00:00');
  games.push(game12);
  var game13 = new Date('September 25, 2015 17:45:00');
  games.push(game13);
  var game14 = new Date('September 26, 2015 15:30:00');
  games.push(game14);
  var game15 = new Date('September 26, 2015 17:45:00');
  games.push(game15);
  var game16 = new Date('September 26, 2015 21:00:00');
  games.push(game16);
  var game17 = new Date('September 27, 2015 13:00:00');
  games.push(game17);
  var game18 = new Date('September 27, 2015 15:30:00');
  games.push(game18);
  var game19 = new Date('September 27, 2015 17:45:00');
  games.push(game19);
  var game20 = new Date('September 29, 2015 17:45:00');
  games.push(game20);
  var game21 = new Date('October 1, 2015 17:45:00');
  games.push(game21);
  var game22 = new Date('October 1, 2015 21:00:00');
  games.push(game22);
  var game23 = new Date('October 2, 2015 21:00:00');
  games.push(game23);
  var game24 = new Date('October 3, 2015 15:30:00');
  games.push(game24);
  var game25 = new Date('October 3, 2015 17:45:00');
  games.push(game25);
  var game26 = new Date('October 3, 2015 21:00:00');
  games.push(game26);
  var game27 = new Date('October 4, 2015 15:30:00');
  games.push(game27);
  var game28 = new Date('October 4, 2015 17:45:00');
  games.push(game28);
  var game29 = new Date('October 6, 2015 17:45:00');
  games.push(game29);
  var game30 = new Date('October 6, 2015 21:00:00');
  games.push(game30);
  var game31 = new Date('October 7, 2015 17:45:00');
  games.push(game31);
  var game32 = new Date('October 7, 2015 21:00:00');
  games.push(game32);
  var game33 = new Date('October 9, 2015 21:00:00');
  games.push(game33);
  var game34 = new Date('October 10, 2015 15:30:00');
  games.push(game34);
  var game35 = new Date('October 10, 2015 17:45:00');
  games.push(game35);
  var game36 = new Date('October 10, 2015 21:00:00');
  games.push(game36);
  var game37 = new Date('October 11, 2015 13:00:00');
  games.push(game37);
  var game38 = new Date('October 11, 2015 15:30:00');
  games.push(game38);
  var game39 = new Date('October 11, 2015 17:45:00');
  games.push(game39);
  var game40 = new Date('October 11, 2015 21:00:00');
  games.push(game40);

  var returnVar = 0;

  for(i = 0; i < 40; i++){
    if(currentTime.getTime() < games[i].getTime()){
        returnVar = i+1;
        break;
    }
  }
  return returnVar;
}

// helper function to improve cross browser support when determining the
// current position

function currentYPosition() {
    // Firefox, Chrome, Opera, Safari
    if (self.pageYOffset) return self.pageYOffset;
    // Internet Explorer 6 - standards mode
    if (document.documentElement && document.documentElement.scrollTop)
        return document.documentElement.scrollTop;
    // Internet Explorer 6, 7 and 8
    if (document.body.scrollTop) return document.body.scrollTop;
    return 0;
}

//Function yto determine the position of thh destination element

function elmYPosition(eID) {
    var elm = document.getElementById(eID);
    var y = elm.offsetTop;
    var node = elm;
    while (node.offsetParent && node.offsetParent != document.body) {
        node = node.offsetParent;
        y += node.offsetTop;
    } return y;
}

//Function to do the scrolling

function smoothScroll() {
    var eID = determine() + "-show";
    var startY = currentYPosition();
    var stopY = elmYPosition(eID);
    var distance = stopY > startY ? stopY - startY : startY - stopY;
    if (distance < 100) {
        scrollTo(0, stopY); return;
    }
    var speed = Math.round(distance / 100);
    if (speed >= 20) speed = 20;
    var step = Math.round(distance / 25);
    var leapY = stopY > startY ? startY + step : startY - step;
    var timer = 0;
    if (stopY > startY) {
        for ( var i=startY; i<stopY; i+=step ) {
            setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
            leapY += step; if (leapY > stopY) leapY = stopY; timer++;
        } return;
    }
    for ( var i=startY; i>stopY; i-=step ) {
        setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
        leapY -= step; if (leapY < stopY) leapY = stopY; timer++;
    }
    return false;
}
