#!/bin/bash
# Must run to install tool

clear
echo "
  _                _  __          
 | |              (_)/ _|         
 | |    _   _  ___ _| |_ ___ _ __ 
 | |   | | | |/ __| |  _/ _ \ '__|
 | |___| |_| | (__| | ||  __/ |   
 |______\__,_|\___|_|_| \___|_|
 
   _____           _        _ _           
 |_   _|         | |      | | |          
   | |  _ __  ___| |_ __ _| | | ___ _ __ 
   | | | '_ \/ __| __/ _` | | |/ _ \ '__|
  _| |_| | | \__ \ || (_| | | |  __/ |   
 |_____|_| |_|___/\__\__,_|_|_|\___|_|   

";

sudo chmod +x uninstall

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/lucifer"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

elif [ "$(uname)" = "Darwin" ]; then
    INSTALL_DIR="/usr/local/lucifer"
    BIN_DIR="/usr/local/bin"
    BASH_PATH="/bin/bash"
    TERMUX=false
else
    INSTALL_DIR="$HOME/.lucifer"
    BIN_DIR="/usr/local/bin"
    BASH_PATH="/bin/bash"
    TERMUX=false

fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[◉] A directory lucifer was found! Do you want to replace it? [Y/n]:" ;
    read -r mama
    if [ "$mama" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/lucifer*"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/lucifer*"
        fi
    else
        echo "[✘] If you want to install you must remove previous installations [✘] ";
        echo "[✘] Installation failed! [✘] ";
        exit
    fi
fi
echo "[✔] Cleaning up old directories...";
if [ -d "$ETC_DIR/pentest01" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/pentest01"
    else
        sudo rm -rf "$ETC_DIR/pentest01"
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/pentest01/lucifer.git "$INSTALL_DIR";
echo "#!$BASH_PATH
python $INSTALL_DIR/lucifer.py" "${1+"$@"}" > "$INSTALL_DIR/lucifer";
chmod +x "$INSTALL_DIR/lucifer";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/lucifer" "$BIN_DIR"
    cp "$INSTALL_DIR/lucifer.cfg" "$BIN_DIR"
else
    sudo cp "$INSTALL_DIR/lucifer" "$BIN_DIR"
    sudo cp "$INSTALL_DIR/lucifer.cfg" "$BIN_DIR"
fi
rm "$INSTALL_DIR/lucifer";


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Tool installed successfully! [✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔]      All is done!! You can execute tool by typing lucifer !       [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installation failed! [✘] ";
    exit
fi
