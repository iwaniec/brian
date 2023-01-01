float xPos;                      // Horizontal position of the ball
float yPos;                      // Veritcal position of the ball
float speed=1;                   // Speed of the ball
int xDir=1;                    // x-direction of ball motion
int yDir=1;                    // y-direction of ball motion
int score=0;                   // Inital score
int lives=10;                   // Number of lives you start with
boolean lost=false;            // Have you lost yet?
PImage mitt;                   // Image of the catcher mitt

void setup()                   //Runs once when program launches
{
  size (800,600);
  smooth();
  xPos=width/2;                // Horizontal start position of ball
  yPos=width/2;                // Veritical start position of ball
  fill(255,255,255);           // Makes the ball and text white
  textSize(20);                // Sets the size of our text
  mitt = loadImage("mitt.png");
  cursor(mitt);
}

void draw()                                      // Loops over and over again
{
  background (100,100,255);                      // Sky color background
  fill(50,200,50);                               // Grass color
  rect(0,height-100, width, 100);
  fill(255,255,255);                             // Makes the ball and text white
  ellipse(xPos,yPos,40,40);                      // Draw the ball

  xPos=xPos+(speed*xDir);                        // update the ball's horizontal position 
  yPos=yPos+(speed*yDir);                        // update the ball's vertical position 
  if (xPos > width-20 || xPos<21)                // Did the ball hit the side?
  {
    xDir=-xDir;                                  // If it did reverse the direction
  }
  if (yPos<21) {yDir=-yDir;}                     // If the ball hits the top, reverse direction
  if (yPos > height - 120)                       // Did the ball hit the bottom?
  {
    yDir=-yDir;                                  // If it did, reverse the direction,
    if(speed> 1) {speed = speed - 0.5;}          // slow the ball,
    lives = lives - 1;                           // And lose a life
    fill(0,255,0);                               // Flash ground color
    rect(0,height-100, width, 100);
  }


  text("score = "+score,10,20);                  // Print the score on the screen
  text("lives = "+lives,width-110,20);           // Print remaining lives
  if (lives<=0)                                  // Check to see if you lost
  {
    textSize(20);
    text("Click to Restart", 325,100);
    noLoop();                                    // Stop looping at the end of the draw function
    lost=true;
  }
}

void mousePressed()                              // Runs whenever the mouse is pressed
{
  speed=speed+0.5;                               // Increase the speed
  if (dist(mouseX, mouseY, xPos, yPos)<=40)      // Did we hit the target?
  {
    score=score+ceil(speed);                     // Increase the score
    speed=speed+0.5;                             // Increase the speed
    yDir = -1;                                   // Change direction
  }
  if (lost==true)                                // If we lost the game, reset now and start over 
  {
    //Reset all variables to initial conditions
    xPos = width/2;
    yPos = 21;
    speed=1; 
    xDir=1;
    yDir=1;
    score=0;
    lives=10;
    lost=false;
    loop();                                     //Begin looping draw function again
  }
}
