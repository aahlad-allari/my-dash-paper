#!/usr/bin/env zx
import start from './main.mjs';

let cmd = argv.c;
let url = argv.url;
let text = argv.text;
let font_size = argv.font_size;
let bg = argv.bg;
let img_name = argv.img_name;
let o = argv.o;
let index = argv.index;
let font_style = argv.font_style


switch (cmd) {
    case "start_static_server":
        await start.start_static_server()
        break;
    
    case "stop_static_server":
        await start.stop_static_server()
        break;

    case "start_magic_mirror":
        await start.start_magic_mirror()
        break;
    
    case "stop_magic_mirror":
        await start.stop_magic_mirror()
        break;

    case "py_calendar":
        await start.py_calendar()
        break;
    
    case "web_calendar":
        await start.web_calendar()
        break;

    case "write_text":
        await start.write_text({text, font_size, orientation: o, font_style: font_style})    
        break;

    case "webpage":
        await start.webpage({url: url, bg: bg, o: o})
        break;

    case "image":
        await start.image({img_name, bg})
        break;
    
    case "web_col":
        await start.web_col({index, o})
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
    
    case "magicmirror":
        await start.magicmirror()
        break;
    
    case "literature_clock":
        await start.literature_clock()
        break;

    default:
        break;
}