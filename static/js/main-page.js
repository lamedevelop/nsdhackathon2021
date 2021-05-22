const send = document.querySelector('div[id=send]')
const income = document.querySelector('div[id=income]')
const outcome = document.querySelector('div[id=outcome]')
const logout = document.querySelector('div[id=logout]')
const settings = document.querySelector('div[id=settings]')

send.addEventListener('click', function (e) {
    post('/send', {}, 'get')
})

income.addEventListener('click', async function (e) {
    let r = await fetch('api/income/data?user_id=2')
    let data = await r.json()

    const content = document.querySelector('.content')
    content.innerHTML = ''

    data.data.forEach(x => {
        let content_message = document.createElement('a')
        content_message.className = 'content-message'
        if (!x.viewed) {
            content_message.className += ' viewed'
        }
        content_message.href = '#'

        let sender = document.createElement('span')
        sender.innerHTML = x.sender
        let message = document.createElement('span')
        message.innerHTML = x.message
        let creation_date = document.createElement('span')
        creation_date.innerHTML = x.creation_date

        content_message.appendChild(sender)
        content_message.appendChild(message)
        content_message.appendChild(creation_date)
        content.appendChild(content_message)
    });

})

outcome.addEventListener('click', async function (e) {
    let r = await fetch('api/outcome/data?user_id=2')
    let data = await r.json()

    const content = document.querySelector('.content')
    content.innerHTML = ''

    data.data.forEach(x => {
        let content_message = document.createElement('a')
        content_message.className = 'content-message'
        if (!x.viewed) {
            content_message.className += ' viewed'
        }
        content_message.href = '#'

        let receiver = document.createElement('span')
        receiver.innerHTML = x.receiver
        let message = document.createElement('span')
        message.innerHTML = x.message
        let creation_date = document.createElement('span')
        creation_date.innerHTML = x.creation_date

        content_message.appendChild(receiver)
        content_message.appendChild(message)
        content_message.appendChild(creation_date)
        content.appendChild(content_message)
    });
})

logout.addEventListener('click', function (e) {
    post('/logout', '')
})

settings.addEventListener('click', function (e) {
    post('/settings', '', 'get')
})