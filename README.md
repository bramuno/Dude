Under construction...

Dude's Harness (tenative title) 

This project is designed to be a failsafe for forgetful pet owners like myself.  Once upon ago, I accidentally left my 15yo dog, Dude, out in the Phoenix summer heat for several hours and he ended up dying from heat stroke. Sadly this is not an uncommon thing in these extreme heat climates.  I thought of this project years ago but never got around to it, so hopefully this will save someone's pet from the same accident. 

This project uses an ESP32 wifi development board connected to two DS18B20 temperature sensors to constantly send temperature readings to a syslog server on the user's home network.  The syslog server runs a cron script to monitor the termperature and alert the user if both sensors have been exceeded the temperature threshold for too long a time period.   

Usage and build instructions coming soon...

I welcome others to assist me with this project to improve wherever possible, so if you would like to collboarte and contribute, please drop me a line.  

<h2>Hardware:</h2>
1 - Raspberry Pi/Odroid<br>
2 - DS18B20 Temperature Sensor<br>
1 - ESP-WROOM-32 ESP32 ESP-32S Development Board <br>
??- LiPo batteries TBD<br>
1 - dog harness TBD<br>
1 - can of Flex Seal Clear<br>
??- Low voltage wires (cat5 cable works great)
<br>
<h3>SMS carriers codes</h3>
0 - Verizon<br>
1 - AT&T<br>
2 - Boost<br>
3 - T-Mobile<br>
4 - Cricket<br>
5 - Sprint<br><br>

Total Power Consumption:<br>
I've connected the <b>ESP32 and both sensors</b> to a power meter and the most power it has used is 80ma, but the average appears to be 30ma.   This does not include the raspberry pi. 
