const registration = document.getElementById('registration-go')

registration.addEventListener('click', function (e) {

    const form_data = document.getElementsByTagName('input')

    const data = {
        name: form_data[0].value,
        email: form_data[1].value,
        phone: form_data[2].value,
        password: form_data[3].value,
    }

    post('/registration', data)
})