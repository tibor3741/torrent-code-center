# Torrent Kódközpont

Az alkalmazás lehetővé teszi a felhasználók számára, hogy könnyen kezeljék és generálják a különböző streaming szolgáltatásokhoz tartozó torrent kódokat. Válassz ki egy streaming szolgáltatást, és az alkalmazás megjeleníti a hozzá tartozó kódot, amit másolhatsz és beilleszthetsz a torrentoldalon. Így könnyedén rá tudsz szűrni azokra a torrentekre, amelyeket a kiválasztott szolgáltatótól szeretnél nézni.

## Használat

1. Válassz ki egy streaming szolgáltatást a bal oldali listából.
2. A jobb oldali listában megjelenik a kiválasztott szolgáltatás torrent kódja.
3. Másold ki a kódot, majd illeszd be a torrentoldalon a keresési lekérdezéshez.

## Telepítés
Klónozd le a projektet a saját számítógépedre.
   ```text
  git clone https://github.com/tibor3741/torrent-code-center
  ```
Navigálj a projekt könyvtárba.
```text 
cd projekt
```
A hozz létre egy virtuális környezetet. 
```text 
python -m venv myenv
```
Aktiváld a virtuális környezetet. A parancs eltér a rendszertől:
Windows-on: 
```text 
.\myenv\Scripts\activate
```
Linux/Mac-en:
```text 
source myenv/bin/activate
```
Telepítsd a szükséges csomagokat.
```text
pip install -r requirements.txt
```
Futtasd az alkalmazást.
```text
python main.py
```

## Tesztelés

Az alkalmazás sikeresen tesztelve lett a következő weboldalakon:
- [nCore](https://ncore.cc)
- [Majomparádé](https://majomparade.hu)
- [1337x](https://1337x.to)
- [Huntorrent](https://huntorrent.net)
- [TorrentGalaxy](https://torrentgalaxy.to)
- [RARBG](https://rarbg.to)

## Programhasználat és Tevékenységek

Az általam készített programot kizárólag az általános információs célokra terveztem, és nem vállalok felelősséget a felhasználók által a program használata során végrehajtott konkrét tevékenységekért, beleértve, de nem kizárólagosan, a letöltéseket és más online interakciókat. A felhasználók saját felelősségükre használják a programot, és vállalják minden tevékenységükért a teljes felelősséget.
