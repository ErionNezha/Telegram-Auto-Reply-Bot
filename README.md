# Telegram Auto-Reply Bot 🤖

Bot Telegram në Python (Telethon) që u përgjigjet **automatikisht** mesazheve private me një mesazh të paracaktuar.

## Si funksionon
Kur dikush i shkruan llogarisë në privat, boti dërgon automatikisht përgjigjen e konfiguruar (në versionin origjinal: një mesazh arabisht që tregon se përdoruesi nuk është i disponueshëm për momentin).

## Si ekzekutohet versioni real
1. Instalo Telethon: `pip install telethon`
2. Merr `API ID` dhe `API Hash` nga https://my.telegram.org
3. Vendosi në `original/bot.py` (variablat `api_id` / `api_hash`)
4. Ekzekuto: `python original/bot.py`
5. Në herën e parë do të kërkohet numri i telefonit + kodi i verifikimit nga Telegram.

> ⚠️ Mos i ndaj me askënd API ID / API Hash — janë kredenciale personale.

## Demo në browser
Dosja `demo/` përmban një **simulim** të bisedës (chat UI si Telegram) ku çdo mesazh merr auto-përgjigjen e botit. Versioni real ekzekutohet vetëm në Python, jo në browser.

---
Krijuar nga **Erion Nezha** — © 2026 Të gjitha të drejtat e rezervuara
