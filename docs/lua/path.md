# Pfade

## Map Ordner

`g_currentMission.missionInfo.map.baseDirectory`

Diese Variable exisitert nur ab dem `loadMap()` vom Spiel aufgerufen wird.

## Mod Ordner

`g_currentModDirectory`

Diese Variable existiert nur beim laden des Skripts.

Man muss diese Variable am Anfang vom Skript laden und **nicht in Funktionen**!

```lua
-- RICHTIG
local modDirectory = g_currentModDirectory

-- FALSCH
function update()
    local modDirectory = g_currentModDirectory
end
```
