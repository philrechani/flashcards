// Sample JSON object
const jsonObject = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "isSubscribed": true
};

export function generateForm(obj) {
    const form = document.createElement('form');

    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            const label = document.createElement('label');
            label.textContent = key + ': ';

            const input = document.createElement('input');
            input.name = key;
            input.id = key;

            // Set input type based on value type
            switch (typeof obj[key]) {
                case 'number':
                    input.type = 'number';
                    break;
                case 'boolean':
                    input.type = 'checkbox';
                    input.checked = obj[key];
                    break;
                default:
                    input.type = 'text';
            }

            input.value = obj[key];

            const div = document.createElement('div');
            div.appendChild(label);
            div.appendChild(input);
            form.appendChild(div);
        }
    }

    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Submit';
    form.appendChild(submitButton);

    return form;
}

