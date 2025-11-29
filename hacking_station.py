import os
import time

# ANSI Farbcodes
GREEN = '\033[92m'
RESET = '\033[0m'

# Start halt
def intro():
    print(GREEN)
    print("""
    
 _   _   ___   _____  _   _ _____  _   _  _____ 
| | | | / _ \ /  __ \| | / /|  ___|| \ | ||  __ \\
| |_| |/ /_\ \| /  \/| |/ / | |__  |  \| || |  \/
|  _  ||  _  || |    |    \ |  __| | . ` || | __ 
| | | || | | || \__/\| |\  \| |___ | |\  || |_\ \\
\_| |_/\_| |_/ \____/\_| \_/\____/ \_| \_/ \____/
                                                  
 _____ _____  ___  _____ _____ _____ _   _ 
/  ___|_   _|/ _ \|_   _|_   _|  _  | \ | |
\ `--.  | | / /_\ \ | |   | | | | | |  \| |
 `--. \ | | |  _  | | |   | | | | | | . ` |
/\__/ / | | | | | | | |  _| |_\ \_/ / |\  |
\____/  \_/ \_| |_/ \_/  \___/ \___/\_| \_/
                                            
    """)
    print(RESET)
    print("="*50)
    print("Willkommen zur EBGS Hacking Station")
    print("Glaubst du du Schaffst es Alle Aufgaben zur Bewältigen")
    print("="*50 + "\n")
    time.sleep(1)


# Challange 2 da Challange 1 Nicht Funktionierte und ich keine Zeit für Debugging habe
def challenge_2():
    print("EBGS Hacking Station")
    print("="*50)
    score = 0
    
    # Teil 1: Netzwerk Discovery
    print("\nTEIL 1: Geräte im Netzwerk finden")
    print("="*50)
    print("\ndu bist in einem fremden WLAN")
    print("Wir wollen jetzt sehen, welche Computer mit dem Schul Wlan verbunden sind")
    print("Dies machen wir mit dem Befehl der sich unter mit Befindet")
    print("\nnmap -sn 192.168.1.0/24")
    print("(Das ist wie eine Schatzkarte für Computer)")
    input("\nDrücke ENTER um zu starten...")
    
    print("\nBitte warten, ich suche nach Geräten...")
    time.sleep(1)
    os.system("nmap -sn 192.168.1.1-10")
    
    answer = input("\nWie viele Geräte hast du gefunden? Schreib eine Zahl: ")
    print("Super Du hast es geschafft! +10 Punkte für Gute Mitarbeit weiter zur Nächsten Station\n")
    score += 10
    time.sleep(2)
    
    # Teil 2: Port Scanning
    print("\n" + "="*50)
    print("TEIL 2: Offene Türen finden (Port Scanner)")
    print("="*50)
    print("\nJeder Computer hat viele Türen (wir nennen sie Ports).")
    print("Manche Türen sind offen, manche sind zu.")
    print("Wir schauen jetzt, welche Türen offen sind!")
    print("\nDer Befehl heisst: nmap -p 1-100 192.168.1.1")
    input("\nDrücke ENTER um die Türen zu checken...")
    
    print("\nSchaue nach offenen Türen...")
    time.sleep(1)
    os.system("nmap -p 22,80,443 localhost")
    
    print("\n--- WICHTIG ---")
    print("Schau auf die Liste oben!")
    print("Dort siehst du die Türen (Ports) und ob sie 'open' oder 'closed' sind.")
    print("'open' = Tür ist offen")
    print("'closed' = Tür ist zu")
    print("\nSuche nach Tür 22 (das ist SSH damit kann man sich einloggen)")
    
    answer = input("\nIst Tür(Port) 22 offen? Schreib 'ja' wenn dort 'open' steht, wenn neben tür 22 aber 'Closed' Steht schreib 'nein': ")
    if "ja" in answer.lower():
        print("Richtig! Gut aufgepasst! +10 Punkte\n")
        print("Du Wirst Langsam immer Besser\n")
        score += 10
    else:
        print("Schau nochmal in der Liste nach der Zahl 22!\n")
        print("Keine Sorge, hier sind trotzdem 5 Punkte für dich da wir gesehen haben das du dir wirklich Mühe gegeben hast\n")
        print("Lass dir Am besten bei der Nächsten Aufgabe mehr Zeit 👍 \n")
        score += 5
    time.sleep(2)
    
    # Teil 3: Service Detection
    # Alles Gut Her Immpelman der Verbindet sich nur mit den Eignen laptop
    print("\n" + "="*50)
    print("TEIL 3: Was macht der Computer?")
    print("="*50)
    print("\nJetzt wollen wir wissen: Was macht der Computer hinter den Türen?")
    print("Ist da eine Website? Oder kann man sich einloggen? oder Finden wir Passwörter???")
    print("\nWir Nutzen darfür den Befehl: nmap -sV localhost")
    input("\nDrücke ENTER um den Befehl Auszuführen...")
    
    print("\nIch schaue nach, was der Computer macht...")
    time.sleep(1)
    os.system("nmap -sV -p 22,80,443 localhost")
    
    print("\nGut gemacht! Du kannst jetzt sehen was läuft! +10 Punkte\n")
    score += 10
    time.sleep(2)
    
    # Teil 4: OS Detection
    print("\n" + "="*50)
    print("TEIL 4: Welches Betriebssystem wird Genutzt?")
    print("="*50)
    print("\nHey da bist du Ja Wieder du hast es schon Echt weit Geschafft")
    time.sleep(1)
    print("\nBist du aber auch für die Aufgabe Bereit?")
    time.sleep(3)
    print("\nLos Gehts!")
    print("\nJetzt finden wir heraus: Was auf den Computer Läuft: Windows, Linux oder Mac? (Windows, Linux, Mac Sind Betriebsysteme das kann man sich wie ein Manager Vorstellen der Alles Steuert)")
    time.sleep(5)
    print("Das ist wichtig für Hacker damit sie sich Anpassen können")
    print("\nDen Befehl den wir Darfür Nutzen heißt: uname -a")
    input("\nDrücke ENTER auf der Tastatur Den Befehl Auszuführen...")
    
    print("\nPrüfung Läuft Bitte Warten...")
    time.sleep(1)
    os.system("uname -a")
    
    answer = input("\nSteht da das der Laptop oder PC Linux nutzt? Schreib ja oder nein: ")
    if "ja" in answer.lower():
        print("SUPER! Du bist aufmerksam! +10 Punkte\n")
        score += 10
    else:
        print("Lies nochmal genauer Vielleicht siehst du es 👀\n")
    time.sleep(2)
    
    # Teil 5: Netzwerk Analyse
    print("\n" + "="*50)
    print("TEIL 5: Netzwerk Adressen finden")
    print("="*50)
    print("\nJeder Computer im Internet hat eine Adresse (Dies kann man sich wie eine Hausnummer auf einer Straße Vorstellen)")
    print("Wir schauen jetzt, welche Adresse(Hausnummer) unser Computer hat")
    print("\nDer Befehl den wir darfür nutzen heißt: ip addr  , Und Zeigt uns was unsere Hausnummer ist :)")
    input("\nDrücke ENTER um den Befehl Auszuführen und die Adresse zu sehen...")
    
    print("\nZeige die Netzwerk Adresse...")
    time.sleep(1)
    os.system("ip addr show | grep inet || ifconfig")
    
    print("\nGUT GEMACHT! Du hast die Hausnummer(Adresse) gefunden +10 Punkte für dich\n")
    score += 10
    time.sleep(2)
    
    # Bonus Challenge
    print("\n" + "="*50)
    print("📶 BONUS: WLAN Netzwerke finden")
    print("="*50)
    print("\nZum Schluss suchen wir nach allen WLANs(Internet) in der Nähe!")
    print("Das ist wie wenn du auf einen Handy nach den WLAN suchst und dich Verbinden willst")
    print("\nDen Befehl den wir darfür nutzen Heißt: nmcli dev wifi")
    input("\nDrücke ENTER um das WLAN zu suchen...")
    
    print("\nSuche nach WLAN Netzwerken...")
    time.sleep(1)
    os.system("nmcli dev wifi || iwconfig")
    
    answer = input("\nHast du WLAN Netzwerke gefunden und sie wurden die Angezeigt? Schreib ja oder nein: ")
    if "ja" in answer.lower():
        print("BONUS PUNKTE! Du bist ein Richtiger Profi +20 Punkte\n")
        score += 20
    else:
        print("Kein Problem ich bin Sicher du hast Trotzdem gut mitgemacht!\n")
    time.sleep(2)
    
    # ende
    print("\n" + "="*50)
    print("GESCHAFFT!")
    print(f"Deine Punkte: {score} von 70 Punkten")
    print("="*50)
    
    if score >= 60:
        print("\nWOW! Du bist ein ELITE HACKER")
    elif score >= 40:
        print("\nSEHR GUT! Du bist ein Wirklich guter Hacker!")
    elif score >= 20:
        print("\nGut Gemacht! Du bist auf dem richtigen Weg!")
    else:
        print("\nGut Mitgemacht!")
    
    print("\n" + "="*50)
    
    # Zusammenfassung
    print("\nDAS HAST DU HEUTE GELERNT:")
    print("  1. Wie man Computer im Netzwerk findet")
    print("  2. Wie man offene Türen (Ports) findet")
    print("  3. Wie man herausfindet was ein Computer macht")
    print("  4. Wie man das Betriebssystem erkennt")
    print("  5. Wie man Netzwerk Adressen findet")
    print("  6. Wie man WLAN Netzwerke Sucht")    
    return score

def main():
    intro()
    challenge_2()
    
    print("\n" + "="*50)
    print("Danke fürs Mitmachen wir von der EBGS Wünschen dir noch viel Spaß")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
