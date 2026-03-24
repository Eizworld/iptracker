#!/bin/bash

clear
echo "Installing Eiz IP Tracker (Color UI)..."

pkg update -y
pkg install python -y

pip install requests colorama pyfiglet

chmod +x iptracker.py

echo ""
echo "Installation Complete!"
echo "Run: python iptracker.py"
