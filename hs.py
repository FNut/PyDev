print('Hacker Simulator')
print('')

print('Login system')
logname = input('Name: ')
logpasswdord = input('Password: ')
print('Done!')
print('')

print('1) Info')
print('2) Aircrack-NG')
utsel = input('Utility: ')

if utsel == ('1'):
    print('Info')
    print('1) Select wifi')
    print('2) Write Aireplay in console')
    print('3) Write Aircrack in console')
    print('You Hack the Wi-Fi!')
    print('Restart this script to start hacking')

if utsel == ('2'):
    print('Aircrack-NG')
    print('')
    print('Wi-Fi')
    print('1) RT-WIFI 1080')
    print('2) TP-LINK_CACEF8')
    print('3) MGTS_1026039')
    print('4) 2kom407')
    print('5) Wi-Fi-Router_2784')
    wifisel = input('Wi-Fi Number: ')
    if wifisel == ('1') or ('2') or ('3') or ('4') or ('5'):
        aireplay = input('>>> ')
        if aireplay == ('aireplay'):
            print('Aireplay')
            print('Find 7063 passwords')
            aircrack = input ('>>> ')
            if aircrack == ('aircrack'):
                print('BruteForce')
                print('Password is: admin')
                print('Done!')
    
