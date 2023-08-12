### *Following this [Twilio Tutorial](https://www.twilio.com/blog/build-live-traffic-whatsapp-chatbot-python-flask-folium-twilio)* 

### Create virtual environment if it doesn't exist:
python3 -m venv shehacks2023-venv

### Open virtual environment
source shehacks2023-venv/bin/activate

### Install dependences
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make install file executable if not:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chmod +x whatsapp_chatbot/install.sh  

./whatsapp_chatbot/install.sh
### Run flask in virtual environment
flask run
### Make application reachable from internet (in separate tab)
ngrok http 5000
### Get URL that is redirected to application
After "Forwarding", the https one
### Add URL to Twilio Sandbox
In "WHEN A MESSAGE COMES IN" field

# ***You are now connected***