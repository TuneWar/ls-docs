# XML Laden

Um eine XML Datei zu laden, muss man die `loadXMLFile` Funktion verwenden.

```lua
local path = "dataS/blabla.xml" -- soll nicht manuell geschrieben sein
local xml = loadXMLFile("newXML", path)
```

## Argumente

| Name       | Beschreibung                                                        |
| ---------- | ------------------------------------------------------------------- |
| objectName | Muss eindeutig sein. Weiss nicht warum GIANTS das so gemacht hat... |
| path       | [Der Pfad von der XML-Datei das GIANTS lädt.](../path.md)           |
