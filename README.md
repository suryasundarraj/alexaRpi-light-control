# Voice Controlled Home Automation using Alexa and Raspberry Pi

This Repo contains the Python script for Amazon Alexa home automation demo using Raspberry Pi . This Repo is the accompanying source code for this [blog series](http://radiostud.io/voice-controlled-home-automation-alexa-part-2/).

## Prerequisites 

- Register Account with [PubNub](www.pubnub.com) 
- Register Account with [IFTTT](www.ifttt.com)
- Register Account with [Amazon Alexa](developer.amazon.com/alexa) 
- Raspbian OS on Raspberry Pi

## Setting up PubNub in RPi 

Step 1: Install pip using following command 

    sudo apt-get install python-pip
    
Step 2: Install pubnub python module to Raspberry Pi using following command 

    sudo pip install 'pubnub>=3,<4'

Step 3: Make sure git is installed in RPi, if not follow this step to install git

    sudo apt-get install git 

## Running this Scrpit on RPi

Step 1: Clone this repo using following command to the Raspberry Pi

    git clone https://github.com/suryasundarraj/alexaRpi-light-control.git

Step 2: Run the script using the following,

    cd alexaRpi-light-control.git
    python alexaRpi.py




