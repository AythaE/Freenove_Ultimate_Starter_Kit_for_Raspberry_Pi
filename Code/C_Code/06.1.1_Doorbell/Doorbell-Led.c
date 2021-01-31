/**********************************************************************
* Filename    : Doorbell-Led.c
* Description : Make doorbell with buzzer, led and button.
* Author      : aythae@gmail.com
* modification: 2021/01/31
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define buzzerPin 0  	//define the buzzerPin
#define buttonPin 1		//define the buttonPin
#define ledPin 4		//define the ledPin

int main(void)
{
	printf("Program is starting ... \n");
	
	wiringPiSetup();
	
	pinMode(buzzerPin, OUTPUT); 
	pinMode(ledPin, OUTPUT); 
	pinMode(buttonPin, INPUT);

	pullUpDnControl(buttonPin, PUD_UP);  //pull up to HIGH level
	while(1){
		
		if(digitalRead(buttonPin) == LOW){ //button is pressed
			digitalWrite(buzzerPin, HIGH);	//Turn on buzzer 
			digitalWrite(ledPin, HIGH);   	//Turn on led 
			printf("Doorbell on >>> \n");
		}
		else {				//button is released 
			digitalWrite(buzzerPin, LOW);   //Turn off buzzer
			digitalWrite(ledPin, LOW);   	//Turn off led 

			printf("Doorbell off <<< \n");
		}
	}
}

