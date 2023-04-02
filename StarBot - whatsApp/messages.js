const {Client} = require('whatsapp-web.js')
const fs = require('fs')

const client = new Client()

client.on('message', message => {
    console.log(message.body)
    fs.writeFile('messages.txt', message.body, (err) => {
        if(err) throw err
    })
})

client.on('message', message => {
    let toSend = ''
    fs.readFile('reply.txt', (err, inputD) => {
        if (err) throw err
        toSend = inputD.toString()
     })

     fs.writeFile('reply.txt', ' ', (err) => {
        if(err) throw err
     })

    message.reply(toSend)
});
 