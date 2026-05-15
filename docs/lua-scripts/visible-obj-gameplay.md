# Visible Obj Gameplay

Mit dieser Lua kannst Du Objekte/Gebäude jeh nach Spielzeit einblenden oder Ausblenden lassen.

Dies soll das Spielerlebnis deutlich verbessern, in dem sich jeh nach Spielzeit die Map verändert.

## Anleitung

1. Kopiere die visibleObjGameplay.lua und die visibleObjGameplay.xml in deine Map unter deineMap/ im gleichen ort wo Du deine ModDesc.xml hast.

2. öffne die ModDesc.xml von deiner Map und trage die Lua ein.
	<extraSourceFiles>
		<sourceFile filename="visibleObjGameplay.lua"/>
	</extraSourceFiles>	

3. öffne deine Map im GE

4. erstelle im Scenegraph unter der Transformgroup (gameplay) eine TransformGroup mit dem z.B "vog_scriptLua"

5. in dem gerade erstellten TransformGroup erstelle noch eine TransformGroup z.B. "vog_deko", und oder "vog_buildings" können beliegig viele sein. Die Gruppenstruktur ist wichtig!

    ```
    - []vog_scriptLua (TransformGroup)
    -- -- []vog_deko (TransformGroup)
    -- -- -- vog_Geruest1 (objekt)
    -- -- -- vog_Geruest2 (objekt)
    -- -- -- vog_Blumen1 (objekt)
    -- -- []vog_buildings (TransformGroup)
    -- -- -- vog_Haus1 (objekt)
    -- -- -- vog_Haus2 (objekt)
    -- -- []usw. (TransformGroup)
    ```

6. Kopiere deine Objekte in die jeweilige Transformgroup.

7. öffne die visibleObjGameplay.xml im NodePad oder in einem Texteditor.

8. In der xml findest Du schon ein Paar Beispiele:

    ```xml
    <object objectName="dekopack/Playground/vog_outsidePool01" playtimeDays="10" visible="false" />
    ```

## Beschreibung

`objectName="vog_scriptLua/vog_deko/vog_boardStackA_PREFAB1"`

vog_boardStackA_PREFAB1 ist der Objekt Name, die Objektnamen dürfen nur einmal vorhanden sein, also einzigartig! Es kann auch eine TransformGroup erstellt werden in der mehrere Objekte enthalten sind. Die Children sind durch `/` getrennt.

`playtimeDays="10"`

Hier wird die Spielzeit in Tage angegeben, wann die Aktionen ausgeführt werden soll.

`visible="false"`

Hier sagst Du bei `false` oder `true` ob das Objekt anzeigen oder ausblenden soll.

## Animation

In der XML muss eine `#!xml <animation />` im `#!xml <object></object>` hinzugefügt werden.

Es gibt diese Attributen im `<animation />`:

- `durationDays`: Dauer in Tage wie lange die Animation geht
- `type`: Was animiert wird. Gerade wird nur `"translate"` (Position) unterstützt.
- `from`: Koordinaten von wo es anfängt.
- `to`: Koordinaten zu wohin es animiert wird.
- `easing` (optional): Animationsart. Standardmässig ist es auf `"linear"`. Liste von Animationsarten gibt es auf <https://easings.net>.

## Beispiel

```xml

<objects>
   <object
        objectName="dekopack/Playground/vog_outsidePool01"
        playtimeDays="10"
        visible="false"
    />  <!-- objekt nach 10 Tagen Spielzeit ausblenden -->
   <object
        objectName="dekopack/Playground/vog_outsidePool02"
        playtimeDays="22"
        visible="true"
    /> <!-- objekt nach 22 Tagen Spielzeit einblenden -->


   <object
        objectName="vog_scriptLua/vog_buildings/vog_residentialHouse03_1_deko"
        playtimeDays="25"
        visible="true"> 
        <animation
            durationDays="0.5"
            type="translate"
            from="5000 10 5000"
            to="5000 30 5000"
        />
   </object>
</objects>
```
