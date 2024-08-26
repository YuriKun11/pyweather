#!/data/data/com.termux/files/usr/bin/bash

ln -s $(pwd)/app.py ~/bin/weather-app

if ! grep -q 'export PATH=$PATH:~/bin' ~/.bashrc; then
    echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
    source ~/.bashrc
fi

echo "Setup complete. You can now run 'weather-app' from anywhere."