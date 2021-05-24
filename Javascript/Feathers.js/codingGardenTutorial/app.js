const feathers = require('@feathersjs/feathers');
const app = feathers();

class MessageService {
    constructor() {
        this.messages = [];
    }
    async find() {
        return this.messages;
    }
    async create(data) {
        const message = {
            id : this.messages.length,
            text : data.text
        }
        this.messages.push(message);
    }
}

app.use('messages', new MessageService());

app.service('messages').on('created', message => {
    console.log('new msg had been created', message);
})

const main = async () => {
    await app.service('messages').create( {
        text : "hello"
    })
    await app.service('messages').create( {
        text : "hello2"
    })

    const messages = await app.service('messages').find();
    console.log('All msgs', messages);

}

main();