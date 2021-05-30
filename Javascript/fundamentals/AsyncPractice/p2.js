https://www.codingame.com/playgrounds/347/javascript-promises-mastering-the-asynchronous/more-pratice-with-promises

function job(data) {
    const result = new Promise( (resolve, reject) => {
        if (typeof(data) == "number") {
            if (data%2 != 0) {
                setTimeout( () => {
                    resolve("odd")
                }, 1000)}
            else {
                    setTimeout( () => {
                        reject("even")
                    }, 2000)
                }
            
        }
        else {
            reject("error")
        }
    })
    return result
    }

module.exports = job;