# ECE444-Lab-Week4&5: Docker Intro
This is Hong Xu, this repo is a clone of https://github.com/miguelgrinberg/flasky

## Activity 1 (1pt): 
Perform all development in a branch "lab4_Microservice_Experiment" in your Lab3 task GitHub repository. 

## Activity 2: Docker and Screenshots
- To build and start, first clone the repository: 

  ` https://github.com/HX001/ECE444-F2020-Lab3/tree/lab4_Microservice_Experiment `
- Check out the branch:

  ` git checkout lab4_Microservice_Experiment`

- Download the docker if you dont have:

  https://docs.docker.com/get-started/
  
- Two way to start:
  - Method 1:
    To build: 
    
    `docker build -t flask-sample:latest .`
    
    To run: 
    
    `docker run -d -p 5000:5000 flask-sample`
    
  - Method 2:
    Simply use docker-compose: 
    
    `docker-compose up`
    
- To check the img:  

  `docker ps -a`

- The **dockerfiles** and **requirements.txt** and **docker-compose.yml** are located in the root directory of this repository:  

  `https://github.com/HX001/ECE444-F2020-Lab3/tree/lab4_Microservice_Experiment`

- The followings are the screenshots:
  - The screenshot of Lab 3 Acitivty 2 application running in docker
    <img src="https://github.com/HX001/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ScreenShot/Lab4/UI.png" height="50%" width="50%">
  
  - The screenshot of container logs
    <img src="https://github.com/HX001/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ScreenShot/Lab4/Container%20Log.png" height="50%" width="50%">
    
  - The screenshot of docker run command 
    <img src="https://github.com/HX001/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ScreenShot/Lab4/Docker%20Run%20Command.png" height="50%" width="50%">
    
  - The screenshot of image status
    <img src="https://github.com/HX001/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ScreenShot/Lab4/Docker%20Image.png" height="50%" width="50%">
   
  - The screenshot of docker-compose
    <img src="https://github.com/HX001/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ScreenShot/Lab4/docker-compose.png" height="50%" width="50%">
    



## Activity 3: Briefly summarize the differences between Docker and Virtual Machine.
Docker | Virtual Machine
------------ | -------------
Docker does not required operating systems, it runs the images and containers on host operating systems | VM creates guest OS above the host OS on host server, then run application inside of it. Every VM runs in it own virtual OS.
Lightweight (KBs/MBs) | Heavyweight (few GBs)
OS level process isolation | Hardware-level process isolation
Require fewer resources, less memory space | Allocate required memory
Process-level isolation, possibly less secure | Fully isolated, more secure
Takes a few seconds to run (In second) | Takes longer time to start a VM (In minutes)
