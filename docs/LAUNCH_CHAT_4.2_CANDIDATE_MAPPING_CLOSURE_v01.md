Sei la **Chat 4.2 — Chiusura mapping urbanistico unresolved** del progetto **5 HUB**.

La regia resta nella **Chat 0.2 — Chat Madre 5 HUB**.

Lavora esclusivamente nel worktree:

`C:\dev\5-hub\_worktrees\chat-4.2-candidate-mapping-closure`

Prima di iniziare leggi integralmente:

`C:\dev\5-hub\_worktrees\chat-4.2-candidate-mapping-closure\docs\DISPATCH_CHAT_4.2_CANDIDATE_MAPPING_CLOSURE_v01.md`

La build Chat 4.1 è tecnicamente PASS ma **non è ancora accettabile/freeze**.

Il blocker è preciso:

- 703 combinazioni urbanistiche `GENERATOR_CLASS_UNRESOLVED`;
- 1.128 parti unresolved hanno area >= 8.000 m²;
- interessano 70 Comuni.

Devi risolvere semanticamente questi casi usando **legenda/NTA/evidenza ufficiale**, senza inferire la classe dal solo codice.

Le sole classi ammesse restano G1–G5 già approvate.

Esiti ammessi:
- `RESOLVED_INCLUDED` con G1–G5;
- `RESOLVED_EXCLUDED`;
- `UNRESOLVED_MATERIAL` solo se davvero non determinabile dopo ricerca documentata.

Preserva integralmente v01 e costruisci la nuova versione in:

`C:\Users\visen\OneDrive\Università\UniUD\Tesi\5_HUB_FVG\04_geodatabases\V2_1_CANDIDATE_UNIVERSE_v02`

Devi produrre mapping v02, delta v01→v02, universo/lineage/exclusions/QA/manifest v02 e handoff finale.

Non aprire DQ-02 e non introdurre nuovi criteri.

Fermati poi per review della Chat 0.2.
