from django.shortcuts import render, redirect
import serial

# Establish connection to Arduino (update the port to match your setup)
try:
    arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Linux example; use 'COM3' on Windows
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None

def control_led(request, action):
    """View to send on/off commands to the Arduino."""
    if arduino:
        if action == 'on':
            arduino.write(b'1')  # Send '1' to turn the LED on
        elif action == 'off':
            arduino.write(b'0')  # Send '0' to turn the LED off
    return redirect('led_control')  # Go back to the main control page

def led_control(request):
    """Render the LED control page."""
    return render(request, 'led_control.html')
