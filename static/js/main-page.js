const send = document.querySelector('div[id=send]')
const income = document.querySelector('div[id=income]')
const outcome = document.querySelector('div[id=outcome]')
const logout = document.querySelector('div[id=logout]')
const settings = document.querySelector('div[id=settings]')

send.addEventListener('click', function (e) {
    post('/send', {}, 'get')
})
income.addEventListener('click', async function (e) {
    let r = await fetch('/api/income?user_id=2')
    let data = await r.json()
    console.log(data)
})
outcome.addEventListener('click', async function (e) {
    let r = await fetch('/api/outcome?user_id=2')
    let data = await r.json()
    console.log(data)
})
logout.addEventListener('click', function (e) {
    console.log(4)
})
settings.addEventListener('click', function (e) {
    console.log(5)
})