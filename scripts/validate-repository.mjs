import { access, readFile } from "node:fs/promises";

const requiredFiles = [
  "README.md",
  "CONTRIBUTING.md",
  "GOVERNANCE.md",
  "SECURITY.md",
  "CODE_OF_CONDUCT.md",
  "AGENTS.md",
  ".github/PULL_REQUEST_TEMPLATE.md",
];

const failures = [];

for (const path of requiredFiles) {
  try {
    await access(path);
  } catch {
    failures.push(`missing required file: ${path}`);
  }
}

for (const path of requiredFiles.filter((path) => path.endsWith(".md"))) {
  try {
    const content = await readFile(path, "utf8");
    if (!content.trim().startsWith("#") && !content.trim().startsWith("<")) {
      failures.push(`${path} must begin with a Markdown or HTML heading`);
    }
    if (/\b(TODO|TBD|FIXME)\b/.test(content)) {
      failures.push(`${path} contains unresolved placeholder language`);
    }
  } catch {
    // Missing files are reported above.
  }
}

if (failures.length) {
  console.error(failures.join("\n"));
  process.exit(1);
}

console.log(`Repository contract verified (${requiredFiles.length} required files).`);
