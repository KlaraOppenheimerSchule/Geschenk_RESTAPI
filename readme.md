# Lokalen Python Server starten (ohne API):

Für den Server benötigt werden die 3 Dateien:  

-APIserver.py  
-index.html  
-myotherpage.html  

1) Diese in einen gemeinsamen Ordner ziehen.
2) Visual Studio Code öffnen
3) Das Terminal in VS Code öffnen (strg + ö)
4) Im Terminal zum Ordner mit den Dateien navigieren (cd <pfad>)
5) "python -m http.server" im Terminal auf dem Ordner-Pfad ausführen
6) Im Terminal sollte etwas stehen wie: "Serving HTTP on :: port 8000 ...."
7) Im Browser per "localhost:8000" kann jetzt auf die Dateien zugegriffen werden.
8) "Hello World etc etc this is the index file" sollte im Browser ausgegeben werden
9) mit "localhost:8000/myotherpage" sollte ein Seitenwechsel möglich sein (auf die "myotherpage.html")
  
 -> Bei dem Server handelt es sich nur um ein zu Testzwecken / Wissensaneignung aufgesetztem Skript; in Sachen API ist hier noch nichts implementiert! 

  
 # Lokalen Python Server starten (mit API):
  
  In diesem Fall werden die Testdateien (index.html / myotherpage.html) nicht mehr benötigt.
  
  1) Über das Terminal kann mit:  "C:/. . ./python.exe C:\. . .\APIserver.py" die Python file ausgeführt werden.
  2) In der APIserver.py wird ein "BaseHTTPRequestHandler" implementiert welcher auch gleich gestartet wird.
  Damit läuft nun auch ein Lokaler Python Server, der die Implementierten http-requests ausführen kann. 
