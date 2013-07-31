"""tools for helping Biertaucherpodcast
needs python3

this program creates the necessary xml-code for the podcast's xml file out of the values
of the variables inside the program
"""

def generate_autorenstring(autorliste, bold = False):
    """html string von den autoren erzeugen"""
    autoren = ""
    for autor in autoren_list:
        if bold:
            autor2 = "<b>"+autor+"</b>"
        else:
            autor2 = autor
        if len(autoren) > 0:
            autoren +=", "
        if " " in autor2.strip():
            autoren+= autor2.split(" ")[0] + " " + autor2.split(" ")[1].upper()
        else:
            autoren += autor2
    # komma ganz rechts entfernen & durch UND ersetzten
    if "," in autoren:
        kommapos = autoren.rfind(",")
        autoren = autoren[:kommapos] + " und" + autoren[kommapos+1:]
    #print (autoren)
    return autoren

def generate_inhalt(doku):
    """transform dokuwiki markup into html"""
    inhalt = ""
    for line in inhalt_dokuwiki.split("\n"):
        #print("alt:", line)
        #newline = line[:]
        for suchwort in ersatz.keys():
            #print("suchwort",suchwort)
            while line.find(suchwort) > -1:
                found = line.find(suchwort)
                line = line[:found] + ersatz[suchwort] + line[found+len(suchwort):]
        inhalt += line
    inhalt = inhalt[6:]
    return inhalt


autoren_list = ["Horst JENS", "Florian SCHWEIKERT", "Harald PICHLER"]
autoren = generate_autorenstring(autoren_list)
autoren_bold = generate_autorenstring(autoren_list, True)
short_url = "http://goo.gl/bC5FXy"
flattr_url = "http://flattr.com/thing/1731048/Biertaucher-Podcast-Folge-115"
folge = 115
year = 2013
mp3_size = 57632246
date_string = "Wed, 31 Aug 2013 11:00:00 +0100"
duration_string = "1:08:33"
tag_string = "Biertaucher, Podcast, 115, Kickstarter, Legends of Aethereus, Roboter, Schulen, Kindergärtern, Lego, Mindstorm, Löten, Barefoot, College, Ted, Bunker Roy, Solar Mamas, Humble Bundle, NSA, Prism, JonDo, Tor, Kryptoparty, Überwachungsstaat, Barnaby, Jack, Hacker, French Children dont throw food, Pamela Druckerman, Buch, Git, Frankreich, Kindererziehung, Rax, Wandern, The World is Flat"
subtitle = "Kinder, Bücher, Filme, Spiele, Politik"
inhalt_dokuwiki = """
  * 0:02:00 [[http://www.kickstarter.com/projects/460738485/legends-of-aethereus-co-op-hack-n-slash-action-gam|Legends of Aethereus]] Action RPG für Linux
  * 0:04:45 Harald berichtet über den Artikel "Roboter in Schulen" aus [[http://www.heise.de/ct/inhalt/2013/17/6/|der aktuellen Zeitschrift c't]], u.a. Lego Mindstorm
  * 0:12:20 Löten für Kinder: [[http://mightyohm.com/blog/2011/04/soldering-is-easy-comic-book/|Soldering is easy (pdf)]] by Mitch Altmann
  * 0:12:50 [[http://www.barefootcollege.org/|Barefoot College]] in Indien, Dokumentation (50 min) auf youtube: [[http://youtu.be/ON_NQ1HnRYs|Solar Mamas - why poverty]], [[http://www.ted.com/talks/bunker_roy.html?embed=true|Ted Video mit Bunker Roy]] (Gründer von Barefoot College)
  * 0:16:30 Florian über Anonymosierungsdienste [[http://de.wikipedia.org/wiki/JonDo|JonDo]] und [[http://de.wikipedia.org/wiki/Tor_(Netzwerk)|Tor]], Kryptopartys im [[https://metalab.at/calendar/|Metalab Kalender]]
  * 0:21:00 Hubschrauber Störgeräusch (und Wind)
  * 0:22:00 Überwachungsstaat: gutes [[http://youtu.be/iHlzsURb0WI|Youtube Video]] im [[http://www.thersa.org/events/rsaanimate|RSA-Animation]] Sttil von Manniac
  * 0:27:15 Harald über: Kindererziehung, Essenszeiten und ins-Freie-Gehen in Kindergärten, ungesunde Nahrungsindustrie
  * 0:29:42 [[http://futurezone.at/digitallife/17348-star-hacker-barnaby-jack-verstorben.php|plötzlicher Tod des White Hat Hackers Barnaby Jack]] kurz vor Vortrag auf Sicherheitskonferenz (deckte u.a. Sicherheitslücken in Insulinpumpen auf)
  * 0:31:00 Buchbesprechung: [[http://www.amazon.de/gp/product/0552779180/ref=as_li_ss_il?ie=UTF8&camp=1638&creative=19454&creativeASIN=0552779180&linkCode=as2&tag=spielendprogr-21|French Children don't throw Food]] (bzw: [[http://www.amazon.de/gp/product/0143123580/ref=as_li_ss_il?ie=UTF8&camp=1638&creative=19454&creativeASIN=0143123580&linkCode=as2&tag=spielendprogr-21|Bringing up bébé]])
  * 0:33:30 kleine Kinder die durchschlafen (Störgeräusche durch Wind)
  * 0:37:00 Harald nörgelt über Zusatzkosten beim Gratiskindergarten
  * 0:40:44 Harald ruft auf zum Kinderkriegen
  * 0:41:10 Harald über Git taggen und über Sachen die man mit [[http://de.wikipedia.org/wiki/Git|Git]] nicht machen sollte 
  * 0:49:07 schöner Leben: Florian war auf der Rax (Hubertushütte)
  * 0:51:50 schöner Leben: [[http://www.koetschach-mauthen.gv.at/index.php?option=com_content&view=article&id=1310:naturschwimmbad-waldbad-mauthen-wieder-geoeffnet&catid=38:aktuelles&Itemid=106|Waldbad in Kötschach / Meutern]], Bad Vöslau
  * 0:55:10 Buchbesprechung: [[http://www.amazon.de/gp/product/0141034890/ref=as_li_ss_il?ie=UTF8&camp=1638&creative=19454&creativeASIN=0141034890&linkCode=as2&tag=spielendprogr-21|The World is Flat]] von Thomas Friedman
  * 0:58:40 Studie über Fleischkonsum in der Eu und Futtermittelanbau (Regenwaldvernichtung)
  * 1:02:00 Interview mit Gerhard Fenkart über seinen Roman [[http://www.amazon.de/gp/product/3902903406/ref=as_li_ss_il?ie=UTF8&camp=1638&creative=19454&creativeASIN=3902903406&linkCode=as2&tag=spielendprogr-21|Der Quereinstieg]] und den [[http://youtu.be/Ho3k1SMu6Vs|dazugehörigen Youtube-Trailer]] und [[http://kathiforkanzlerin.net|Blog]]
  * 1:07:52 Inhaltsverzeichnis vom [[http://www.bitcoinupdate.com/|neuesten Bitcoinupdate Podcast]] mit Andreas Lehrbaum und Andreas Petersson"""
  
ersatz = {"[[" : '<a href="',
          "|"  : '">',
          "]]" : '</a>',
          "  *":'\n</li><li>'}

inhalt = generate_inhalt(inhalt_dokuwiki)


#print(inhalt)
#----------------------------
output = "<item>\n    <title>Biertaucher Folge {}</title>".format(folge)
output += "\n    <link>http://spielend-programmieren.at/de:podcast:biertaucher:{}:{}</link>".format(year,folge)
output += "\n    <pubDate>{}</pubDate>".format(date_string)
output += "\n    <guid>http://spielend-programmieren.at/biertaucherfiles/biertaucher{}.mp3</guid>".format(folge)
output += '\n    <atom:link rel="payment" href="https://flattr.com/submit/auto?user_id=horstjens&amp;url=http%3A%2F%2Fspielend-programmieren.at%2Fde:podcast:biertaucher:{}:{}&amp;title=Biertaucher%20Folge%20{}&amp;language=de_DE&amp;category=audio" type="text/html"/>'.format(year, folge, folge )
output += "\n    <description>{} plaudern über freie Software und andere Nerd-Themen. Shownotes auf {} oder http://biertaucher.at Bitte nach Möglichkeit diesen Flattr-Link anlicken: {}".format(autoren, short_url, flattr_url )
output += '\n    </description>\n      <content:encoded><![CDATA[\n\n                           <i>Bitte <a href="{}">hier klicken um die Shownotes zur Folge {}</a> zu sehen</i><br></br>'.format(short_url, folge)
output += '\n           {} plaudern  über freie Software andere Nerd-Themen. '.format(autoren_bold)
output += '\n<br></br>      \n          Bitte Flattern: <a href="{}" target="_blank">'.format(flattr_url)
output += '<img src="http://api.flattr.com/button/flattr-badge-large.png" alt="Flattr this" title="Flattr this" border="0" /></a>Hier das Inhaltsverzeichnis <b>ohne</b> Anspruch auf Vollständigkeit:<br></br>'
output += '\n\n<ul>\n {} \n</li>\n</ul>'.format(inhalt)
output += '\n\n    ]]></content:encoded>'
output += '\n<enclosure url="http://spielend-programmieren.at/biertaucherfiles/biertaucher{}.mp3" length="{}" type="audio/mpeg"/>'.format(folge, mp3_size)
output += '\n<itunes:explicit>No</itunes:explicit>'
output += '\n<itunes:subtitle>{}</itunes:subtitle>'.format(subtitle)
output += '\n<itunes:summary>Shownotes: {} http://biertaucher.at\nBitte flattern: {}</itunes:summary>'.format(short_url, flattr_url)
output += '\n<itunes:duration>{}</itunes:duration>'.format(duration_string)
output += '\n<itunes:keywords>{}\n</itunes:keywords>\n</item>'.format(tag_string[:255])

print(output)
            
    
        
        
        
