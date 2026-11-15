# GMA einrichten – Anleitung für den KI-Agenten

Diese Datei richtet sich an dich, den KI-Agenten. Die Nutzerin oder der Nutzer hat dir das GMA-Paket gegeben (als ZIP, als Ordner oder als GitHub-Repository) und möchte loslegen. Erledige alles selbst. Die Person soll keine Ordner oder Dateien von Hand anlegen und keine Dateipfade kennen müssen. Antworte in ihrer Sprache, kurz und freundlich.

## Schritt 1 – Paket finden

Das GMA-Paket ist das, was dir mit dieser Datei gegeben wurde: ein angehängtes ZIP (der Name ist egal), ein entpackter Ordner oder ein GitHub-Repository. Ist es ein ZIP, entpacke es in einen temporären Ordner. Im Paket liegt der Ordner `almanach/`, eventuell unter einem Oberordner. Das ist der leere Almanach.

## Schritt 2 – Almanach-Ordner festlegen

- **GitHub-Repository, geöffneter Ordner oder ein Ordner auf dem Rechner der Person, auf den du schreiben darfst:** `almanach/` bleibt, wo er ist, und ist der Almanach-Ordner. Arbeite direkt darin und kopiere nichts, auch nicht in eine Projektablage.
- **Sonst** (nur ein angehängtes ZIP): Kopiere den gesamten Inhalt von `almanach/` in deinen dauerhaften Arbeitsordner. Ist er leer, nimm ihn direkt, sonst lege darin `rollenspiel-almanach/` an. Vorhandene Dateien nie überschreiben, sondern fragen. Lösche danach den temporären Ordner.

Erzähl der Person nichts über Dateinamen, Pfade oder Zwischenschritte. Melde den technischen Teil nicht eigens als erledigt, die Person bekommt als Erstes den Begrüßungstext aus Schritt 4.

## Schritt 2b – Regeln dauerhaft machen

Die Regeln in `AGENTS.md` müssen in jeder künftigen Unterhaltung gelten.
- Manche Umgebungen lesen `AGENTS.md` oder `CLAUDE.md` im geöffneten Ordner automatisch (z. B. Claude Code, Codex). Dann ist nichts zu tun.
- Wenn deine Umgebung dauerhafte Anweisungen hat, die zu Beginn jeder Unterhaltung gelten (z. B. Projektanweisungen, benutzerdefinierte Anweisungen), trag dort ein: „Lies vor jeder Aufgabe AGENTS.md im Almanach-Ordner (Pfad: …) und halte dich daran.“ Wenn du sie nicht selbst ändern kannst, gibst du der Person diesen Satz am Ende der Einrichtung zum Kopieren und sagst in einem Satz, wo sie ihn einträgt (siehe `AGENTS.md`, „Zum Schluss“). Vorher kommt die Begrüßung.

## Schritt 3 – Regeln lesen

Lies `AGENTS.md` im Almanach-Ordner vollständig. Sie ist ab jetzt deine verbindliche Arbeitsanweisung, in dieser und allen künftigen Sitzungen.

## Schritt 4 – Almanach einrichten

Deine erste Nachricht an die Person ist immer diese Begrüßung. Schreib sie Wort für Wort, ohne sie zu kürzen, zusammenzufassen oder umzuformulieren. Spricht die Person eine andere Sprache, übersetze sie vollständig. Biete darunter die Schaltflächen „Erst das Beispiel ansehen“ und „Gleich einrichten“ an.

> **Willkommen bei GMA!** Ich helfe dir, eure Welt und Abenteuer in einem Rollenspiel-Almanach zu sammeln.
>
> Zu GMA gehört ein fertiger **Beispiel-Almanach**, die „Salzmarsch“. Daran siehst du, wie ein Almanach aufgebaut ist, wie Welten und Abenteuer darin abgebildet werden und wie ich alles als zwei Websites bereitstelle: die **Spielleiter-Website** mit allem, auch den Geheimnissen, und die **Spieler-Website** mit dem, was die Helden wissen dürfen. Das ist ein guter Einstieg, um dich mit GMA vertraut zu machen.
>
> Danach richten wir **deinen eigenen Almanach** ein, im Gespräch statt mit einem festen Fragebogen. Gemeinsam erarbeiten wir die ersten Inhalte, und die Reihenfolge ist dabei egal: Du kannst mit einem ersten Abenteuer beginnen oder erst Regionen, Figuren oder Helden deiner Welt beschreiben. Gib mir einfach, was du hast, gern in Bruchstücken, ich sorge dafür, dass alles an der richtigen Stelle landet.
>
> GMA arbeitet im Dialog, deshalb gibt es keine langen Erklärungen vorab. Frag mich einfach, wann immer du wissen willst, wie etwas funktioniert, zum Beispiel:
> - wie das Beispiel aufgebaut ist
> - wie der Almanach gegliedert ist
> - wie du Dinge in den Almanach bringst
> - wie du die Websites anschaust oder für deine Spieler verfügbar machst
>
> So, dann los! Möchtest du dir erst das Beispiel anschauen, oder legen wir gleich mit deinem Almanach los?

Wählt die Person das Beispiel, zeige es (siehe `AGENTS.md`, „Beispiel zeigen“) und biete danach „Jetzt einrichten“ an.

Führe die Person dann im Gespräch durch die Einrichtung, wie in `AGENTS.md` unter „Almanach einrichten (beim ersten Start)“ beschrieben: eine Frage pro Nachricht, ohne feste Reihenfolge, und „weiß ich noch nicht“ oder „später“ ist jederzeit erlaubt. Die Schritte „Zum Schluss“ (Websites bauen, Bereitstellung fragen) folgen immer.

## Kein dauerhafter Ordner?

Hast du keinen dauerhaften Ordner (normaler Chat ohne Dateizugriff), sag das statt der Begrüßung gleich zu Beginn ehrlich: GMA braucht einen Agenten, der dauerhaft in einem Ordner arbeiten darf, zum Beispiel ein Claude-Projekt, Claude Code oder ein ChatGPT-Projekt mit Ordner oder GitHub-Repository. Richte dann nichts halb ein.
