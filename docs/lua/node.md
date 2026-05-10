---
icon: material/cube
---

# Node

## Node holen

Um ein Node zu holen aus der Map:

```lua
function splitString(text, sep)
    local splitted = {}
    local progress = ""
    for index = 1, #text do
        local character = string.sub(text, index, index)
        if character == sep then
            table.insert(splitted, progress)
            progress = ""
        else
            progress = progress .. character
        end
    end
    table.insert(splitted, progress)
    return splitted
end

function getNodeByPath(path, rootNode)
    local node = rootNode
    local splitted = splitString(path, "/")
    if not node then
        node = getParent(g_currentMission.terrainRootNode)
    end
    if node == nil or node == 0 then
        return nil
    end
    for _, v in ipairs(splitted) do
        node = getChild(node, v)
        if node == nil or node == 0 then
            return nil
        end
    end
    return node
end
```

Um es zu benutzen (`rootNode` Parameter ist optional):

```lua
local node = getNodeByPath("transformGroup1/testObjekt")
if node ~= nil then
    -- ...
else
    -- ...
end
```

## Alle Children

Um alle Children anzeigen zu lassen:

```lua
function treeChildren(node, recursion)
    local prefix = ""
    for i = 1, recursion do
        prefix = prefix .. "- "
    end
    if recursion > 4 then
        log(prefix .. " !!! LIMIT REACHED!")
        return
    end
    log(prefix .. getName(node))
    for i = 0, getNumOfChildren(node) - 1 do
        treeChildren(getChildAt(node, i), recursion + 1)
    end
end

treeChildren(getRootNode(), 0)
```
