#!/usr/bin/python3

#This program imports the 'urllib.request' subpackage
#and the 'smtplib' package to run some functions

def URLlib():
    import urllib.request as url

    with url.urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as m:
        for line in m:
            line = line.decode()
            """converts byte to string"""
            if line.startswith("datetime"):
                print(line.rstrip())
                """remove trailing new line"""
'''
def SMTPLIB():
    import smtplib as sm

    server = sm.SMTP('localhost')
    server.sendmail("soothsayer@example.org", "jcaesar@example.org",
    """To: jcaesar@example.org
    From: soothsayer@example.org

    Beware the Idea of April
    """)
    server.quit()    
'''
URLlib()
#SMTPLIB()
print("\nCode developed by Masino")
