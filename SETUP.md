# Setup

1. Public repo named exactly `Arun597134`. Upload README.md, `assets/`, `scripts/` and `.github/` (keep the folder structure).
2. Settings -> Actions -> General -> Workflow permissions -> **Read and write permissions** -> Save.
3. Actions tab -> "Generate Profile Graphics" -> **Run workflow**. Wait about 1 minute. This creates the `output` branch with:
   - `activity.svg`  (Timeline Activity card from YOUR real GitHub data)
   - `snake.svg` (Loki/TVA-style contribution graph + snake, from YOUR real data)
   It refreshes every 6 hours automatically.
4. If a card shows "TIMELINE SYNC FAILED", open the failed run in the Actions tab and read the log.
5. Project demos: record each project (ScreenToGif) and overwrite with the SAME file names:
   assets/demos/civicflow.gif, hirewise.gif, exam-portal.gif, enterprise-ingestion.gif
6. Profile -> Contribution settings -> tick "Private contributions" to include private-repo activity.
