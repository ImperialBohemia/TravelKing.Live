# Jak napojit Google Site na doménu www.travelking.live

Aby se web zobrazoval na vaší doméně, musíte udělat tyto kroky:

## Krok 1: Google Sites Nastavení
1. Otevřete editor Google Site: https://sites.google.com/d/1Kc8GEiGzgo2YdyzDViq1T8NXQpipjQwF/edit
2. Klikněte na **Ozubené kolo (Settings)** vpravo nahoře.
3. Vyberte **Custom Domains** (Vlastní domény).
4. Klikněte **Start Setup**.
5. Zadejte `www.travelking.live`.
6. Google vás požádá o ověření vlastnictví (přes DNS TXT záznam).

## Krok 2: cPanel DNS Nastavení (server707.web-hosting.com)
1. Přihlaste se do cPanelu.
2. Jděte do **Zone Editor**.
3. U domény `travelking.live` klikněte na **Manage**.
4. **CNAME Záznam:**
   - Name: `www`
   - Type: `CNAME`
   - Record: `ghs.googlehosted.com`
   
   *(Pokud tam už záznam pro `www` je, upravte ho. Pokud je to A záznam, smažte ho a vytvořte CNAME).*

5. **TXT Záznam (pro ověření):**
   - Vložte TXT kód, který vám dal Google v Kroku 1.

## Krok 3: Čekat
- Změna DNS může trvat 1 hodinu až 24 hodin.
- Poté bude web dostupný na `https://www.travelking.live`.

**Důležité:** Toto nastavení přesměruje `www`. Pro holou doménu (`travelking.live` bez www) musíte v cPanelu nastavit **Redirect** na `https://www.travelking.live`.
