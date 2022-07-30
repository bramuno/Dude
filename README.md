Under construction...

This project is designed to be a failsafe for forgetful pet owners like myself.  This year I got accidentally left my 15yo dog, Dude, out in the Phoenix summer heat for several hours and he ended up dying from heat stroke. Sadly this is not an uncommon thing in these extreme heat climates.  I thought of this project years ago but never got around to it, so hopefully this will save someone's pet from the same accident. 

This project uses an ESP32 wifi development board connected to two DS18B20 temperature sensors to constantly send temperature readings to a syslog server on the user's home network.  The syslog server runs a cron script to monitor the termperature and alert the user if both sensors have been exceeded the temperature threshold for too long a time period.   

Usage and build instructions coming soon...

I welcome others to assist me with this project to improve wherever possible, so if you would like to collboarte and contribute, please drop me a line.  

Hardware:
1 - Raspberry Pi 
2 - DS18B20 Temperature Sensor
1 - ESP-WROOM-32 ESP32 ESP-32S Development Board 
??- LiPo batteries TBD
1 - dog harness TBD

SMS carriers codes:
0 - Verizon
1 - AT&T
2 - Boost
3 - T-Mobile
4 - Cricket
5 - Sprint
