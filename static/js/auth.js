const registration = document.getElementById('registration-go')

registration.addEventListener('click', function (e) {

    const form_data = document.getElementsByTagName('input')

    const data = {
        email: form_data[0].value,
        password: form_data[1].value,
    }

    post('/login', data)
})