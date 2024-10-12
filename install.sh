#!/bin/bash

if [ -L "/usr/local/bin/labnotes" ]; then
    sudo rm "/usr/local/bin/labnotes"
fi

if [ -d "/usr/local/bin/labnotes_files" ]; then
    sudo rm -r "/usr/local/bin/labnotes_files"
fi

if [ -z "$projects_path" ];then
    while : ; do
        echo -n "path to your projects dir: "
        read pathToProjects
        if [ -d "$pathToProjects" ]; then
            echo "export projects_path=$pathToProjects" >> $HOME/.bashrc
            break
        else
            echo "$pathToProjects doesn't exists, try again."
        fi
    done
fi

if [ "$1" == "local" ];then
    sudo cp -r src /usr/local/bin/labnotes_files
else
    wget http://github.com/nonzeroexit/labnotes/archive/master.zip -O /tmp/labnotes.zip
    unzip -o /tmp/labnotes.zip -d /tmp
    sudo cp -r /tmp/labnotes-main/src /usr/local/bin/labnotes_files
fi
cd /usr/local/bin
sudo ln -s /usr/local/bin/labnotes_files/labnotes.py labnotes
sudo chmod a+rx labnotes
bash
