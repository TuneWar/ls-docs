# Table

Eine Table ist eine Datenstruktur um mehrere Daten in eine Variable zu halten.

Man kann eine Tabelle in zwei Wegen in Lua benutzen:

- Arrays
- Dictionaries

Anders als andere Programmiersprachen, fangen Arrays in Lua mit 1 statt 0 an.

## Beispiele

### Tabelle erstellen

Eine Tabelle erstellen (`{}` heisst neue Tabelle):

```lua
local objects = {}
```

### Tabelle füllen

Eine Tabelle mit Daten befüllen ohne Key (wie als Array benutzt):

```lua
table.insert(objects, "Apfel")
table.insert(objects, "Birne")

--[[


Die Tabelle sieht dann so aus:

local objects = {
    [1] = "Apfel",
    [2] = "Birne",
}


]]
```

Eine Tabelle mit Daten befüllen mit Key (wie als Dictionary benutzt):

```lua
objects["newKey"] = "newValue"
objects["money"] = 400

--[[


Die Tabelle sieht dann so aus:

local objects = {
    ["newKey"] = "newValue",
    ["money"] = 400,
}


]]
```

### Daten einzeln rausholen

Um Daten aus eine Tabelle rauszuholen, benutzt man `[]`:

#### Array

```lua
local objects = {}
table.insert(objects, "Apfel")
table.insert(objects, "Birne")

local wert = objects[1] -- In Lua fangen Arrays mit 1 an

-- "wert" ist jetzt "Apfel"

print(wert) -- gibt "Apfel" aus
```

#### Dictionary

```lua
local objects = {}
objects["money"] = 800
objects["points"] = 300

local wert = objects["money"]

-- "wert" ist jetzt 800

print(wert) -- gibt "800" aus
```

### Alle Daten rausholen (for-loop)

Um eine Array rauszuholen benutzt man `ipairs` (index/value), aber für ein Dictionary benutzt man `pairs` (key/value).

#### Array

```lua
local objects = {}

table.insert(objects, "Apfel")
table.insert(objects, "Birne")

for index, value in ipairs(objects) do
    print("Index", index) -- Index ist dann 1 und 2
    print("Value", value) -- Value wird dann "Apfel" und "Birne" sein
    print()
end


--[[
Index	1
Value	Apfel

Index	2
Value	Birne
]]
```

#### Dictionary

```lua
local objects = {}

objects["money"] = 800
objects["points"] = 600

-- pairs statt ipairs! key statt index!
for key, value in pairs(objects) do
    print("Key", key) -- Key ist dann "money" und "points"
    print("Value", value) -- Value wird dann 800 und 600 sein
    print()
end


--[[
Key    points
Value  600

Key    money
Value  800
]]
```

### Grösse der Tabelle

Um die Grösse der Tabelle zu holen, benutzt man `#` vor der Tabellenname:

```lua
local objects = {"Apfel", "Birne"}

local anzahl = #objects

print(anzahl) -- 2
```

### Tabelle erstellen (fortgeschritten)

"Array" und "Dictionary" gemischt:

```lua
local newTable = {}

-- Hier fügt man Daten zur Tabelle wie ein Array hinzu
table.insert(newTable, "Apfel")
table.insert(newTable, "Birne")

-- Hier fügt man Daten zur Tabelle wie ein Dictionary hinzu
newTable["money"] = 500
newTable["points"] = 700

-- Hier wird nochmals ein Wert zur Tabelle wie ein Array hinzugefügt
table.insert(newTable, "nochmal ein wert")


-- Darstellung
print("Key", "Wert")
print("-------------------")
-- pairs kann auch durch Arrays durchgehen
for i,v in pairs(newTable) do
    print(i,v)
end

--[[
Key       Wert
-------------------
1         Apfel
2         Birne
3         nochmal ein wert
points    700
money     500
]]
```
