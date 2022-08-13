#!/usr/bin/env zx
import {generate_image} from "./web_components/capture_webpage.js"
// $.verbose = false
const log = async (txt) =>{
    await $`echo ${txt}`
}
const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}
let c = argv.c;
let url = argv.url;
let text = argv.text;

let start_static_server = async () => {
    await log("Starting Static Server....")
    let http_static_server = await $`which http-server`
    await $`pm2 start ${http_static_server} --name my-dash-paper-static -- -o ./Widgets/LocalWeb -p 3009 -d false`
}

let stop_static_server = async () => {
    await log("Stopping Static Server....")
    await $`pm2 stop my-dash-paper-static`
}

let write_to_screen = async (mode, text) => {
    await $`echo Writing image to the screen image....`
    await $`python3 orchestrator.py ${mode} ${text}`
}

let default_func = async () => {
    await $`echo Capturing image....`
    generate_image()
    await write_to_screen("text")
}

let load_web_calendar = async () => {
    load_webpage("http://127.0.0.1:3009/Widgets/LocalWeb/Calendar/cal")
}

let load_webpage = async (url = "http://google.com") => {
    let resp = await generate_image(url)
    $`echo Generated Umage....`
    await sleep(10000);
    await write_to_screen("image")
}

let load_py_calendar = async () => {
    await write_to_screen("py_calendar")
}

let wite_text = async (text) => {
    $`echo hhhhhhhh ${text}`
    await write_to_screen("text", text)
}

let hackernews = async (text) => {
    $`echo hhhhhhhh ${text}`
    await write_to_screen("hackernews")
}

switch (c) {
    case "start-static-server":
        await start_static_server()
        break;
    
    case "stop-static-server":
        await stop_static_server()
        break;

    case "py-calendar":
        await load_py_calendar()
        break;
    
    case "web-calendar":
        await load_web_calendar()
        break;

    case "text":
        await wite_text(text)
        break;

    case "web-page":
        await load_webpage(url)
        break;

    case "hackernews":
        await hackernews(url)
        break;

    default:
        break;
}

// let date = await $`date`
// await $`echo Current date is ${date}.`
