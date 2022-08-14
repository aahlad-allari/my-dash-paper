#!/usr/bin/env node
import {$, sleep} from 'zx'
// await $`date`
import moment from "moment";
import yaml from 'js-yaml';
import * as fs from 'fs'
import * as R from 'ramda';
import start from './main.mjs';

const widgets = yaml.load(fs.readFileSync('./widgets.yml', 'utf8'));


const rotate_widgets = async () =>{
    let now = moment().format('MMMM Do YYYY, h:mm:ss a')
    let wdgs = widgets.widgets
    let rand_index = Math.floor(Math.random()*wdgs.length)
    let widget = wdgs[rand_index]

    await $`echo [${now}]: Refreshing a widget with ${widget.name}`
    
    let arg_values = R.values(widget.args)
    if(R.length(arg_values) > 0){
        console.log(widget.cmd, arg_values)
        start[widget.cmd](...arg_values)
    }else{
        start[widget.cmd]()
    }
    
}




const start_background_setver = async () => {
    await start.stop_static_server()
    await sleep(2000)
    await start.flush_logs()
    await start.start_static_server()
    await sleep(2000)
    const wait_in_mins = 5
    setInterval(rotate_widgets, wait_in_mins * 60 * 1000);
    // rotate_widgets()
}

start_background_setver()