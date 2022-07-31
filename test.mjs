#!/usr/bin/env zx

await $`echo Capturing image....`
await $`node web_components/capture_webpage.js`
await $`echo Writing image to the screen image....`
await $`python3 orchestrator.py`

let date = await $`date`
await $`echo Current date is ${date}.`