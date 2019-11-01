# This script sets up the bluetooth device, used with an xbox controller - run this to get the controller ready

su root
sudo echo 1 > /sys/module/bluetooth/parameters/disable_ertm
bluetoothctl
