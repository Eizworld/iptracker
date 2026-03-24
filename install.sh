#!/bin/bash

clear
echo "======================================="
echo "  Installing Eiz IP Tracker Pro Toolkit"
echo "======================================="

pkg update -y
pkg install python -y

pip install requests colorama pyfiglet

chmod +x iptracker.py

echo ""
echo "Installation Complete!"
echo "Run tool using: python iptracker.py"
