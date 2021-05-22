const registration = document.getElementById('registration-go')


function post(path, params, method = 'post') {
    const form = document.createElement('form');
    form.method = method;
    form.action = path;
    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const hiddenField = document.createElement('input');
            hiddenField.type = 'hidden';
            hiddenField.name = key;
            hiddenField.value = params[key];
            form.appendChild(hiddenField);
        }
    }
    document.body.appendChild(form);
    form.submit();
}

registration.addEventListener('click', function (e) {

    const form_data = document.getElementsByTagName('input')

    data = {
        name: form_data[0].value,
        email: form_data[1].value,
        phone: form_data[2].value,
        password: form_data[3].value,
    }

    post('/registration', data)
})