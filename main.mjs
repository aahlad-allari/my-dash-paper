#!/usr/bin/env node
import {$} from 'zx'
import {generate_image} from "./web_components/capture_webpage.js"
// $.verbose = false
const log = async (txt) =>{
    await $`echo ${txt}`
}
const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}


const start = {

    start_static_server: async () => {
        await log("Starting Static Server....")
        let http_static_server = await $`which http-server`
        await $`pm2 start ${http_static_server} --name my-dash-paper-static -- -o ./Widgets/LocalWeb -p 3009 -d false`
    },

    stop_static_server: async () => {
        await log("Stopping Static Server....")
        await $`pm2 stop my-dash-paper-static`
    },

    flush_logs: async () => {
        await $`pm2 flush my-dash-paper-static`
        await log("Flushed logs for static server....")
    },

    write_to_screen: async (mode, text, fontsize=24) => {
        // await $`echo Writing image to the screen image.... ${mode} ${text} ${fontsize}`
        await $`python3 orchestrator.py ${mode} ${text} ${fontsize}`
    },

    default_func: async () => {
        await $`echo Capturing image....`
        generate_image()
        await start.write_to_screen("text")
    },

    web_calendar: async () => {
        start.webpage("http://127.0.0.1:3009/Widgets/LocalWeb/Calendar/cal")
    },

    webpage: async (url = "http://google.com") => {
        let resp = await generate_image(url)
        $`echo Generated Umage....`
        await sleep(10000);
        await start.write_to_screen("image")
    },

    py_calendar: async () => {
        await start.write_to_screen("py_calendar")
    },

    write_text: async (text, fontsize) => {
        await start.write_to_screen("text", text, fontsize)
    },

    hackernews: async (text) => {
        await start.write_to_screen("hackernews")
    },

    dadjoke: async () => {
        $`echo Dad Joke`
        start.write_to_screen('dadjoke')
    },

    greetings: async () => {
        await log("Greetings....")
        start.webpage("http://127.0.0.1:3009/Widgets/LocalWeb/Greetings/greetings")
    },

    weather: async () => {
        await log("Weather....")
        start.webpage("http://127.0.0.1:3009/Widgets/LocalWeb/Weather/")
    },

    py_weather: async () => {
        await start.write_to_screen("py_weather")
    },
    magicmirror: async () => {
        let uname_node = await $`uname -n`
        // Need to run magicmirror as server in the background
        const url = (uname_node == "raspberrypi") ? "http://127.0.0.1:8080/" : "http://192.168.68.116:8080/"
        start.webpage(url)
    },
}

export default start;