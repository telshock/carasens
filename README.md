# carasens
Onboard environmental sensor terminal firmware word salad

------

This "firmware" for a raspberry pi interfaces different sensors, aggregates the data and displays it on a display and/or stores it in a database or cloud. 

## Components
### Itsy Bitsy Sensor Assembly
The Raspberry Pi doesn't have to care what sensors are used. It expects the data on TX/RX in JSON.
### e-Ink Display
Quirky display that needs about 15 seconds to draw a picture in black/red/white. Used to display the sensor data.
### Buttons
You can press them and then the raspberry pi does stuff.
### Database / Cloud connection
This component allows write access to the database/cloud. It also reads from the connection to display historic data.
