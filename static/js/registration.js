const registration = document.getElementById('registration-go')

registration.addEventListener('click', function (e) {

    const form_data = document.getElementsByTagName('input')

    data = {
        name: form_data[0].value,
        email: form_data[1].value,
        phone: form_data[2].value,
        password: form_data[3].value,
    }

    fetch('http://127.0.0.1:8000/api/registration', {
        method: 'POST',
        body: JSON.stringify(data)
    }).then(x => x.json()).then(x => console.log(x))
})