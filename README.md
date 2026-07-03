# PerGen

This repository contains my attempt at creating a simple dataset for LLM training.

## Overview

Everything in this project was "vibe coded" in Sep/Oct 2025 using Deep Research in the Perplexity app from the Samsung store. At the time, Samsung users were being offered a year of Pro subscription for free.

By default, I kept my search assistant set to Sonar/Best, but Deep Research was a separate mode and I specifically used that mode for this project.

My goal was to create datasets for training a model from scratch and giving it a high school level education.

This project is still ongoing. Life got messy for a period of time, but I am now sorting through and picking up the threads of the work. A lot has changed in the industry since then, so parts of this project may need to be revised or discarded.

## Dataset status

- Nothing in this dataset has been reviewed by a human.
- There may be a duplicate file in the repository. Please double-check before use.
- I plan to remove any duplicate content during cleanup.
- I am still verifying token counts, sanitization, cleaning, and deduplication.
- I included a README for each dataset once I remembered to add one.
- The original prompts used to create the dataset files are included under `DEV` with the scripts. I may have veered away from this, but I tried my best to keep track of my methods.

## Repository contents

- `DEV/` — scripts used to convert the original CSV files to JSONL, along with the original prompts.
- Dataset files — the generated synthetic training data in JSONL format (there is 1 JSON).
- Per-dataset README files — included where available.

## License and attribution

A formal license will be added later.

For now, this repository is intended for free use, subject to the request that you cite:
- **Droid Spectre**
- **DroidSpectre/PerGen**

This notice may change once the final license is written.

## Notes

This repository is still being cleaned up, verified, and organized. Use caution before training or distributing derived work.
