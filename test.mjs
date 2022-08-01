#!/usr/bin/env zx
import {generate_image} from "./web_components/capture_webpage.js"
// $.verbose = false
const log = async (txt) =>{
    await $`echo ${txt}`
}
let c = argv.c;

let start_static_server = async () => {
    await log("Starting Static Server....")
    let http_static_server = await $`which http-server`
    await $`pm2 start ${http_static_server} --name my-dash-paper-static -- -o ./Widgets/LocalWeb -p 3009 -d false`
}

let stop_static_server = async () => {
    await log("Stopping Static Server....")
    await $`pm2 stop my-dash-paper-static`
}

let write_to_screen = async () => {
    await $`echo Writing image to the screen image....`
    await $`python3 orchestrator.py`
}

let default_func = async () => {
    await $`echo Capturing image....`
    generate_image()
    await write_to_screen()
}

let load_calendar = async () => {
    await generate_image("http://127.0.0.1:3009/Widgets/LocalWeb/Calendar/cal")
    await $`python3 orchestrator.py`
}

switch (c) {
    case "start-static-server":
        await start_static_server()
        break;
    
    case "stop-static-server":
        await stop_static_server()
        break;

    case "load-calendar":
        await load_calendar()
        break;

    default:
        break;
}

// let date = await $`date`
// await $`echo Current date is ${date}.`
