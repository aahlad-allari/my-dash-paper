#!/usr/bin/env node
import {$} from 'zx'

// $.verbose = false
const log = async (txt) =>{
    await $`echo ${txt}`
}
const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}


const start_daemon =  async () => {
    await log("Starting Daemon service......")
    let http_static_server = await $`which http-server`
    await $`pm2 start scheduler.mjs --name my-dash-paper-daemon`
}

const stop_daemon =  async () => {
    await log("Stop Daemon service......")
    let http_static_server = await $`which http-server`
    await $`pm2 stop scheduler.mjs --name my-dash-paper-daemon`
    await $`pm2 delete my-dash-paper-daemon`
}

const start = argv.start;
const stop = argv.stop;

if(start){
    start_daemon()
    
}

if(stop){
    stop_daemon()
}