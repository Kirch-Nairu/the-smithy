import { readFile } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const [html, css, script] = await Promise.all([
  readFile(new URL("apps/pixel-smithy/dist/index.html", root), "utf8"),
  readFile(new URL("apps/pixel-smithy/dist/canon.css", root), "utf8"),
  readFile(new URL("apps/pixel-smithy/dist/game.js", root), "utf8"),
]);

const requiredHtml = ["danceButton", "danceStage", "danceClose", "kirch-dancer", "danceMusic", "t=120s"];
const requiredCss = ["@keyframes dance-hop", "@keyframes arm-left", "@keyframes leg-left", "prefers-reduced-motion"];
const requiredScript = ["start=120", "openDance", "closeDance", "Escape", "youtube-nocookie.com"];

for (const token of requiredHtml) if (!html.includes(token)) throw new Error(`Dance markup is missing ${token}`);
for (const token of requiredCss) if (!css.includes(token)) throw new Error(`Dance styling is missing ${token}`);
for (const token of requiredScript) if (!script.includes(token)) throw new Error(`Dance behavior is missing ${token}`);

console.log("Dance break verified: choreography, 2:00 music cue, close behavior, and reduced motion are present.");
