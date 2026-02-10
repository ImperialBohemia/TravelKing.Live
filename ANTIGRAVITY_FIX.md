# Antigravity Dialog Fix - Oprava "Closed or Reopen" Dialog

## Problém
Po každém startu Antigravity se objevoval otravný dialog s otázkou, jestli chceš konverzaci zavřít (closed) nebo znovu otevřít (reopen).

## Řešení
Byla provedena úprava konfiguračních souborů Antigravity na 3 úrovních:

### 1. VS Code User Settings
**Soubor:** `/home/q/.config/Antigravity/User/settings.json`

Přidáno:
```json
"gemini.conversations.promptToRestoreOnStartup": false,
"gemini.conversations.autoRestore": false
```

### 2. Gemini CLI Settings
**Soubor:** `/home/q/.gemini/settings.json`

Přidána sekce:
```json
"conversations": {
  "promptToRestoreOnStartup": false,
  "autoRestore": "never",
  "restoreBehavior": "none"
}
```

### 3. Global Storage State
**Soubor:** `/home/q/.config/Antigravity/User/globalStorage/storage.json`

Přidáno:
```json
"gemini.conversations.doNotPromptRestore": true,
"antigravity.conversations.skipRestoreDialog": true
```

## Jak to ověřit

1. **Zavřít** Antigravity úplně (všechna okna)
2. **Restartovat** Antigravity
3. Dialog "closed or reopen" by se **neměl** objevit

## Backup
Záloha původní konfigurace: `/home/q/TravelKing.Live/antigravity_settings_backup.json`

## Změněné soubory
- ✅ `/home/q/.config/Antigravity/User/settings.json`
- ✅ `/home/q/.gemini/settings.json`  
- ✅ `/home/q/.config/Antigravity/User/globalStorage/storage.json`

## Pokud problém přetrvává

Pokud by dialog stále vyskakoval, můžeme zkusit:
1. Vymazat cache konverzací: `rm -rf /home/q/.gemini/antigravity/conversations/*.pb`
2. Resetovat state database: `rm /home/q/.config/Antigravity/User/globalStorage/state.vscdb*`
3. Přidat další nastavení do workspace-specific konfigurace

---
**Datum opravy:** 2026-02-10  
**Status:** ✅ Implementováno - čeká na restart Antigravity pro ověření
