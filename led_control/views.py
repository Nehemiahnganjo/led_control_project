from django.shortcuts import render, redirect
import serial

# Attempt to establish a connection to Arduino
try:
    arduino = serial.Serial('COM4', 9600)  # Update 'COM3' to your actual port
    print("Connected to Arduino.")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None

def reconnect_arduino():
    """Function to attempt reconnecting to the Arduino."""
    global arduino
    try:
        arduino = serial.Serial('COM3', 9600)  # Update 'COM3' as needed
        print("Reconnected to Arduino.")
    except Exception as e:
        print(f"Failed to reconnect to Arduino: {e}")

def control_led(request, action):
    """View to send on/off commands to the Arduino."""
    global arduino
    if arduino:
        try:
            if action == 'on':
                arduino.write(b'1')  # Send '1' to turn the LED on
                print("LED turned ON.")
            elif action == 'off':
                arduino.write(b'0')  # Send '0' to turn the LED off
                print("LED turned OFF.")
        except Exception as e:
            print(f"Error communicating with Arduino: {e}")
            reconnect_arduino()  # Attempt to reconnect if communication fails
    else:
        print("Arduino connection not established.")
        reconnect_arduino()
    return redirect('led_control')

def led_control(request):
    """Render the LED control page."""
    context = {'arduino_connected': arduino is not None}
    return render(request, 'led_control.html', context)
