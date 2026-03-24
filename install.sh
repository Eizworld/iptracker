#!/bin/bash

clear
echo "================================="
echo "   Installing Eiz IP Tracker"
echo "================================="

pkg update -y
pkg install python -y

pip install requests

chmod +x iptracker.py

echo ""
echo "Installation Complete!"
echo "Run tool using: python iptracker.py"
