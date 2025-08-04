# Thermon
Thermon is a utility terminal app which can control a Philips Hue smart plug.
I have created this tool to turn on/off a ventillator once the temperature reaches a certain degree.

<img width="200" height="435" alt="Make a icon showing a Philips Hue Smart plug and Python  Make it look modern and cartoon-ish" src="https://github.com/user-attachments/assets/0095b09b-f234-45da-8aac-edec2abaaff4" />

```python
/c/users/user/coding/thermon
> python .\main.py -t 50
Turned ventilator ON at 50.0°C
```

### Tool
This tool is not meant to be ran on its own. It's meant to be called by other apps which check room temperature and weather conditions. This can be achieved by using it as a terminal app.

### Logging
Logging is used for debugging. Once something does not go acording to the parameters set in the *config.toml* you will be able to find what went wrong.
```terminal
2025-08-01 16:18 - INFO - Turned ventilator ON at 45.0°C
2025-08-01 16:19 - INFO - No change - Temp: 44.0°C, Fan already ON
2025-08-01 16:19 - INFO - Turned ventilator OFF at 35.0°C
2025-08-01 16:19 - INFO - No change - Temp: 36.0°C, Fan already OFF
2025-08-01 18:03 - INFO - No change - Temp: 36.0°C, Fan already OFF
2025-08-03 15:26 - INFO - Turned ventilator ON at 50.0°C
```

### Config
In the *config.toml* file you can find the parameters meant to be set to suit your situation. The IP addres of the Philips Hue Bridge is defined here, as is the name of the Smart Plug.<br>

##### Minimum and Maximum Temperatures<br>
In the *config.toml* file you can set a threshold to make sure the ventillator will not turn on/off every single call. <br>
In this example case, which I have used for cooling my Raspberry PI 
```
[system]
high_temp = 40                  # Highest temperature of the PI
low_temp = 35                   # Lowest temperature threshold of the PI
```
If the temperature of the Raspberry PI exceeds or is equal to the value of **high_temp**. The ventillator will turn on until the temperature is lower or equal to the value of **low_temp**
