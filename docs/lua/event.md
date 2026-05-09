# Events

Mit den Events in LS können während des Spielens verschiedene Funktionen (z. B. Map laden, Maus bewegen) aufgerufen werden.

Um auf Events zu hören, muss man `addModEventListener` benutzen:

```lua
local mod = {}

function mod:loadMap()
    -- Wenn die Map geladen wurde
end

addModEventListener(mod)
```

Im Beispiel haben wir nur auf `loadMap` gehört, aber es gibt viele andere Events die man drauf hören kann.

## `loadMap(filename)`

Wird aufgerufen wenn die Map geladen wurde. Danach ist auch die globale Variable `g_currentMission` gültig.

- `filename`: Pfad von die .i3d Datei

## `update(deltaTime)`

Wird jede Frame aufgerufen nachdem man "START" beim Laden gedrückt hat.

- `deltaTime`: Millisekunden seit dem letzen Frame.

## `mouseEvent(x, y, isDown, isUp, buttonType)`

Wird aufgerufen wenn man die Maus bewegt, die Maus drückt, loslässt oder scrollt.

**ACHTUNG:** Die Werte `isDown`, `isUp`, `buttonType` sind alle Standardwerte wenn man die Maus bewegt. Es ist also nicht möglich, im selben Aufruf zu prüfen, ob die Maustaste gedrückt ist oder nicht.

### Argumente

- `x`: Wert von 0 (links) bis 1 (rechts).
- `y`: Wert von 0 (**unten**) bis 1 (**oben**).
- `isDown`: Boolean-Wert, der angibt, ob die Maustaste gedrückt wurde. Beim Scrollen ist dieser Wert immer `false`.
- `isUp`: Boolean-Wert, der angibt, ob die Maus losgelassen wurde. Beim Scrollen ist dieser Wert immer `true`.
- `buttonType`: Eine Nummer von der Art "mouseEvent". [Die Liste kann man hier finden](input.md#maus)

### Alle `buttonType`s

- `0`: Kein Button (bewegen)
- `1`: Linksklick
- `2`: Mittelklick
- `3`: Rechtsklick
- `4`: Scroll up
- `5`: Scroll down

## `keyEvent(unicode, sym, modifiers, isDown)`

- `sym`: Die Taste. [Die Liste kann man hier finden](input.md#liste)
- `isDown`: Wenn die Taste gedrückt wird.

## `deleteMap()`

Wird aufgerufen wenn die Map geschlossen wird.
