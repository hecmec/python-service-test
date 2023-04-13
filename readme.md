# Services in python

## some videos

How to Create a systemd Linux Service: https://www.youtube.com/watch?v=C4a7jxlMTfo

Running Python Script as a Linux Service (Tal-zvon): https://www.youtube.com/watch?v=hg-YWVz6J-Y
with nice python script

## some code

https://github.com/tal-zvon/python_linux_service/tree/master/main_scripts

Save this file as add_numbers.service in the `/etc/systemd/system/` directory.

Start the service and enable it to start at boot time by running the following commands:

    sudo systemctl daemon-reload
    sudo systemctl start calculator
    sudo systemctl enable calculator

    Now, you can test the service by running the following command:


    sudo systemctl status calculator

This should show that the service is running.
To test the service, run the following command, replacing 5 and 10 with the numbers you want to add:

    sudo systemctl start calculator.service

This should print the result of adding the two numbers.
You can also stop the service using the following command:

    sudo systemctl stop add_numbers

That's it! You now have a systemd service that adds two numbers and can be run from the command line.

    sudo systemctl isolate myservice-add.service -- 5 10
