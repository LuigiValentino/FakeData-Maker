from flask import Flask, render_template, request
from faker import Faker

app = Flask(__name__)
faker = Faker()



FIELDS_MAP = {
    'name': faker.name,
    'email': faker.email,
    'address': faker.address,
    'dob': faker.date_of_birth,
    'phone': faker.phone_number,
    'ssn': faker.ssn,
    'gender': lambda: faker.random_element(elements=('Male', 'Female', 'Other')),
    'city': faker.city,
    'country': faker.country,
    'postcode': faker.postcode,
    'latitude': faker.latitude,
    'longitude': faker.longitude,
    'username': faker.user_name,
    'ipv4': faker.ipv4,
    'mac_address': faker.mac_address,
    'domain_name': faker.domain_name,
    'url': faker.url,
    'credit_card': faker.credit_card_number,
    'credit_card_expiry': faker.credit_card_expire,
    'credit_card_cvv': faker.credit_card_security_code,
    'iban': faker.iban,
    'currency': faker.currency_name,
    'company': faker.company,
    'catch_phrase': faker.catch_phrase,
    'job': faker.job,
    'company_phone': faker.phone_number,
    'company_email': faker.company_email,
    'product_name': faker.word,
    'barcode_ean13': faker.ean13,
    'color': faker.color_name,
    'sentence': faker.sentence,
    'text': faker.text,
    'paragraph': faker.paragraph,
    'license_plate': faker.license_plate,
    'vin': faker.vin,
    'date_time': faker.date_time,
    'month': faker.month,
    'day_of_month': faker.day_of_month,
    'day_of_week': faker.day_of_week,
    'uuid': faker.uuid4,
    'sha256': faker.sha256,
    'color_name': faker.color_name,
    'language_name': faker.language_name,
    'twitter_profile': lambda: f"@{faker.user_name()}",
    'linkedin_url': faker.url,
    'instagram_username': faker.user_name
}

def generate_fake_data(fields, count):
    data_list = []
    for _ in range(count):
        fake_data = {field: FIELDS_MAP[field]() for field in fields if field in FIELDS_MAP}
        data_list.append(fake_data)
    return data_list

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fields = request.form.getlist('fields')
        count = int(request.form['count'])
        data = generate_fake_data(fields, count)
        return render_template('index.html', data=data, fields=fields, count=count, tab='basic')
    
    return render_template('index.html', data=[], fields=[], count=0, tab='basic')

@app.route('/advanced', methods=['GET', 'POST'])
def advanced():
    if request.method == 'POST':
        fields = request.form.getlist('fields')
        count = int(request.form['count'])
        data = generate_fake_data(fields, count)
        return render_template('index.html', data=data, fields=fields, count=count, tab='advanced')
    
    return render_template('index.html', data=[], fields=[], count=0, tab='advanced')

if __name__ == '__main__':
    app.run(debug=True)
