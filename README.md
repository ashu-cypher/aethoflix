# AethoFlix

A self-hosted, Netflix-style browse UI for movies and TV shows — designed to run on
your PC and open on your TV's web browser over your home Wi-Fi.

- Original design (no Netflix branding, no sign-in forms)
- Real metadata: posters, ratings, overviews, trailers (TMDB-sourced, 52 titles)
- Hero carousel, rows incl. Top 10, search, genre filters, detail modal, My List
- **TV-remote friendly**: arrow-key / D-pad navigation, big visible focus rings,
  Enter/OK to open, Back/Escape to close
- One self-contained `index.html` — no build step, no backend needed

> This project only browses metadata. It does not stream, download, or link to
> unlicensed sources.

## Watch it on your TV (same Wi-Fi)

**1. Get the files on your PC**
```bash
git clone https://github.com/ashu-cypher/aethoflix
cd aethoflix
```

**2. Start the server**
```bash
python3 serve.py
```
It prints an address like `http://192.168.1.5:8000/`.

**3. Open it on the TV**

In your TV's web browser, type that address. Navigate with the remote's
arrow keys + OK button.

**If the TV can't reach it:** allow Python through your PC's firewall
(Windows: "Allow an app through firewall"; the TV and PC must be on the
same Wi-Fi network, not a guest network or mobile hotspot with isolation).

**To stop:** Ctrl+C in the terminal.
