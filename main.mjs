#!/usr/bin/env node
import {$} from 'zx'
import * as R from 'ramda';

import {generate_image} from "./web_components/capture_webpage.js"
import web_images  from "./image_urls.mjs"
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

    start_magic_mirror: async () => {
        await log("Starting Static Server....")
        let http_static_server = await $`which http-server`
        await $`cd ~/Documents/proj/magicmirror/MagicMirror && pm2 start "npm run start" --name my-magic-mirror`
    },

    stop_magic_mirror: async () => {
        await log("Stopping Static Server....")
        await $`pm2 stop my-magic-mirror`
    },

    write_to_screen: async (options) => {
        let mode = options.mode
        let arg1 = options.text

        let fontsize = options.fontsize
        let bg = options.bg
        let arg2 = fontsize
        if(bg){
            arg2 = bg
        }
        // await $`echo Writing image to the screen image.... ${mode} ${text} ${fontsize}`
        await $`python3 orchestrator.py ${mode} ${arg1} ${arg2}`
    },

    default_func: async () => {
        await $`echo Capturing image....`
        generate_image()
        await start.write_to_screen({mode: "text"})
    },

    web_calendar: async () => {
        start.webpage({url: "http://127.0.0.1:3009/Widgets/LocalWeb/Calendar/cal"})
    },

    literature_clock: async () => {
        start.webpage({url: "https://literature-clock.jenevoldsen.com/"})
    },

    web_col: async (options) => {
        let index = options.index ? options.index : web_images.length-1
        let o = options.o

        let filter = n => true
        let filtered_list = web_images
        if(index == "r"){
            if(o == 'p' || o == 'P'){
                filter = n => (n.o === 'p' || n.o === 'P');
            } else if((o == 'l')){
                filter = n => (n.o !== 'p' && n.o !== 'P');
            }

            filtered_list = R.filter(filter, web_images)
            index = Math.floor(Math.random() * filtered_list.length)
        }


        console.log("Index...", index)
        const c_image = filtered_list[index]
        console.log(c_image)
        start.webpage(c_image)
    },

    webpage: async (options) => {
        let url = options.url
        let bg = options.bg
        let orientation = options.o
        orientation = orientation ? orientation : "L"
        let resp = await generate_image(url, orientation)
        $`echo Generated Umage....`
        await sleep(10000);
        await start.write_to_screen({mode:"image", bg, text: "image.png"})
    },

    image: async (options) => {
        await start.write_to_screen({mode:"image", text: options.img_name, bg: options.bg})
    },

    py_calendar: async () => {
        await start.write_to_screen({mode:"py_calendar"})
    },

    write_text: async (options) => {
        let text, fontsize = options
        await start.write_to_screen({mode:"text", text, fontsize})
    },

    hackernews: async (text) => {
        await start.write_to_screen({mode:"hackernews"})
    },

    dadjoke: async () => {
        $`echo Dad Joke`
        start.write_to_screen({mode:'dadjoke'})
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
        await start.write_to_screen({mode:"py_weather"})
    },
    magicmirror: async () => {
        let uname_node = await $`uname -n`
        // Need to run magicmirror as server in the background
        const url = (uname_node == "raspberrypi") ? "http://0.0.0.0:8080/" : "http://192.168.68.116:8080/"
        start.webpage(url)
    },
}

export default start;