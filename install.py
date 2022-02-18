import os
choice = input('[+] to install press (Y) to Cancel/Uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 ipbouncer.py')
    run('mkdir /usr/share/aut')
    run('cp ipbouncer.py /usr/share/aut/ipbouncer.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/ipbouncer.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/ipbouncer.py')
    print('''\n\ncongratulation IP BOUNCER is installed successfully nn\nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] now IP BOUNCER has been removed successfully')
