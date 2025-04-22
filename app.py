from flask import Flask, render_template_string, request

app = Flask(__name__)
internships = []

@app.route('/', methods=['GET', 'POST'])
def internship_form():
    if request.method == 'POST':
        title = request.form.get('title')
        company = request.form.get('company')
        location = request.form.get('location')
        if title and company and location:
            internships.append({
                "title": title,
                "company": company,
                "location": location
            })
    
    form_template = '''
    <form method="POST">
        <h2>Post an Internship</h2>
        Title: <input type="text" name="title" required><br>
        Company: <input type="text" name="company" required><br>
        Location: <input type="text" name="location" required><br>
        <button type="submit">Submit</button>
    </form>
    <h3>Posted Internships:</h3>
    <ul>
        {% for internship in internships %}
            <li>{{ internship.title }} at {{ internship.company }} ({{ internship.location }})</li>
        {% endfor %}
    </ul>
    '''
    return render_template_string(form_template, internships=internships)

if __name__ == '__main__':
    app.run(debug=True)