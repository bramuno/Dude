Under construction...

Dude's Harness (tenative title) 

This project is designed to be a failsafe for forgetful pet owners like myself.  Once upon ago, I accidentally left my 15yo dog, Dude, out in the Phoenix summer heat for several hours and he ended up dying from heat stroke. Sadly this is not an uncommon thing in these extreme heat climates.  I thought of this project years ago but never got around to it, so hopefully this will save someone's pet from the same accident. 

This project uses an ESP32 wifi development board connected to two DS18B20 temperature sensors to constantly send temperature readings to a syslog server on the user's home network.  The syslog server runs a cron script to monitor the termperature and alert the user if both sensors have been exceeded the temperature threshold for too long a time period.   

Usage and build instructions coming soon...

I welcome others to assist me with this project to improve wherever possible, so if you would like to collboarte and contribute, please drop me a line.  

<h2>Hardware:</h2>
links provided here are only examples as you can swap out brands as needed to save money as long as the part does what it required, any by all means if you can find it somewhere else then you don't need amazon :)<br>
1 - Raspberry Pi/Odroid<br>
2 - DS18B20 Temperature Sensor<br>
1 - ESP-WROOM-32 ESP32 ESP-32S Development Board <br>
??- LiPo batteries, 3.7vdc TBD<br>
1 - dog harness TBD<br>
1 - can of <a href="https://a.co/d/3PqRW9W">Flex Seal Clear</a><br>
??- Low voltage wires (cat5 cable works great)<br>
3 - M to F <a href="https://a.co/d/5lMv7FR">jumper wires</a> bu if you dont have any, it's cheaper to get the <a href="https://a.co/d/bJQuteo">multi-pack</a>
1 - toggle switch <a href="https://www.amazon.com/s?k=arduino+toggle+switch+3-pole&crid=1M6LX2AWXVDJG&sprefix=arduino+toggle+switch+3-pol%2Caps%2C154&ref=nb_sb_noss">3-pole</a> any style is ok<br>
1 - <a href="https://a.co/d/4tNPrfw">solderable breadboard</a> (optional for experienced users)<br>

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
