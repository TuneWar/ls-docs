# Globals

Um Liste von etwas zu holen:

```lua
function list(toGet)
    print("--- List of table ---")
    for i,v in pairs(toGet) do
        print(i)
    end
    print("---------------------")
end

-----

list(g_currentMission.missionInfo.map)
```
