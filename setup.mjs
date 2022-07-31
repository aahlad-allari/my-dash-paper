#!/usr/bin/env zx

let date = await $`date`
let uname_node = await $`uname -n`

await $`echo Current date is ${date}.`

await $`echo Install Python dependencies....`
if(uname_node == "raspberrypi"){
    await $`pip install .`
}else{
    await $`pipenv install`
}
await $`echo Installing Node dependencies`
await $`npm install`
