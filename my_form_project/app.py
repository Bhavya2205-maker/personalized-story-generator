from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/story', methods=['POST'])
def generate_story():
    # Get all the details from the form
    nickname = request.form['nickname']
    age = request.form['age']
    doing = request.form['doing']
    tech_interest = request.form['tech_interest']
    hobbies = request.form['hobbies']

    # Create a personalized story using all the details
    story = f"""
    Once upon a time, there was a programmer named {nickname} who was a proud {age}-year-old. 
    One day, {nickname} was feeling quite {doing}.
    To cheer themselves up, they decided to combine their love for {tech_interest} with their favorite pastime, {hobbies}.
    They built a program that could do their {hobbies} for them, but it got a little out of control.
    It began coding so fast that the universe started glitching, proving that some interests are best kept separate!
    """

    # Render the new story.html template and pass the 'story' variable to it
    return render_template('story.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)