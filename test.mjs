#!/usr/bin/env zx
import start from './main.mjs';

let cmd = argv.c;
let url = argv.url;
let text = argv.text;
let fontsize = argv.fontsize;


switch (cmd) {
    case "start_static_server":
        await start.start_static_server()
        break;
    
    case "stop_static_server":
        await start.stop_static_server()
        break;

    case "py_calendar":
        await start.py_calendar()
        break;
    
    case "web_calendar":
        await start.web_calendar()
        break;

    case "write_text":
        await start.write_text(text, fontsize)
        break;

    case "webpage":
        await start.webpage(url)
        break;

    case "hackernews":
        await start.hackernews(url)
        break;
    
    case "dadjoke":
        await start.dadjoke()
        break;
    
    case "weather":
        await start.weather()
        break;

    case "py_weather":
        await start.py_weather()
        break;

    default:
        break;
}