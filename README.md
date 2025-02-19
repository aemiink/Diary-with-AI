<p align="center">
  <img src="https://i.ibb.co/5gT19qfN/Screenshot-2025-02-19-143915.png" width="500px">
</p>
<h1 align="center" > Programmer's Diary - A Developer's Journey</h1>



# 🎮 Overview
Programmer's Diary is a collection of personal coding experiences, challenges, and solutions encountered during software development. It serves as a knowledge base, helping developers document their journey and revisit lessons learned over time.

# 🏆 Features

<b><i>Daily Coding Logs: </i></b> Track your progress and reflect on your learning experiences.

<b><i>Project Highlights:</i></b> Document key projects, architecture decisions, and challenges faced.

<b><i>Code Snippets & Solutions: </i></b> Store reusable code snippets for future reference.

<b><i>Bug Tracking & Fixes: </i></b> Maintain a log of encountered bugs and their solutions.

<b><i>Technology Insights: </i></b> Explore new technologies and document findings.

# 🛠️ Technologies Used

<ul>
  <li><b><i> Markdown (For easy documentation and formatting) </i></b></li> 
  <li><b><i>Python / JavaScript / HTML / CSS / JINJA2  (Example languages for code snippets)</i></b></li>
  <li><b><i>Git & GitHub (Version control and repository management)</i></b></li>
  <li><b><i> AI Integratition (For Speech to Write)</i></b></li>
  <li><b><i>Notion / Obsidian / Joplin (Optional: Personal knowledge management tools)</i></b></li>
</ul>


# 📜 Game Modes

<ul>
  <li><b><i>Red Light Green Light:</i></b> Players must stop when the doll turns around, or they get eliminated.</li>
  <li><b><i> Dalgona (Honeycomb Game):  </i></b> Players must carve a shape without breaking the candy.</li>
  <li><b><i> Glass Bridge: </i></b> Players must step on the correct glass panels to cross.</li>
  <li><b><i> Mingle: </i></b> Players must find a partner in time, or they get eliminated.</li>
  <li><b><i> Squid Game: </i></b> The final battle with strategic movement and combat mechanics.</li>
  <li><b><i> Tug of War: </i></b> A physics-based pulling game requiring teamwork and timing.</li>
</ul>


# 🚀 How to Use
<ol>
  <li>
    Clone the repository:
    
    git clone ```https://github.com/aemiink/Diary-with-AI.git```
  </li>
  <li>
    Start Logging Entries
      Create a new Markdown file for each log entry.
      Follow a structured template for consistency.
  </li>
  <li>
    Organize Code Snippets
      Use proper file naming conventions.
      Categorize by programming language or topic.
  </li>
  <li>
    Contribute & Share
      If this is a collaborative project, feel free to submit pull requests.
  </li>
</ol>


# 📜 Example Log Entry
```text
# Date: 2025-02-19
## What I Worked On
- Implemented a state machine for NPC behavior in Unity.
- Refactored some inefficient loops in a game AI system.

## Challenges Faced
- Debugging unexpected behavior in physics interactions.
- Optimizing frame rates for mobile performance.

## Solutions & Learnings
- Used the Unity Profiler to identify bottlenecks.
- Switched from Update() to FixedUpdate() for physics-related logic.
```


# 📚 Librarires
<div display="flex">
   <ol>
     <li><b><i> Flask: </i></b> A lightweight WSGI web application framework for building web applications in Python.</li>
     <li><b><i> Flask SQL Alchemy: </i></b>  A SQL toolkit and Object Relational Mapper (ORM) for Flask applications.</li>
     <li><b><i> Werkuezg Security: </i></b> A module providing password hashing utilities and security tools for Flask applications.</li>
     <li><b><i> Jinja2: </i></b> A templating engine for Python, used in Flask to dynamically render HTML templates.</li>
     <li><b><i> Virtual Enviorement: </i></b> A dependency management tool for Python that creates virtual environments and manages package dependencies efficiently.</li>
   </ol>
</div>

# 💻 Code Snippets
```python
# Database Creating
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Card {self.id}>'
```

```python
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']
        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create_card.html')
```

```jinja2
        <!-- Integration HTML with Flask API -->
        {% block content %}
        <form action="{{ url_for('form_create') }}" method="post" class="creat-form">
            <div class="form__card">
                <img class="card__img" src="../static/img/post_icon.png" width="250" height="250" alt="post_icon">
                <div class="form__inputs">
                    <label for="title">
                        <input class="form__input" type="text" name="title" id="title" placeholder="Girdinin başlığını girin" required>
                    </label>
                    <label for="subtitle">
                        <input class="form__input" type="text" name="subtitle" id="subtitle" placeholder="Girdinin açıklamasını girin" required>
                    </label>
                </div>
                <label for="text">
                    <textarea class="form__text" name="text" id="text" cols="30" rows="10" required placeholder="Girdiyi buraya yazın..."></textarea>
                </label>
                <button class="form__button">Oluştur</button>
            </div>
        </form>
        {% endblock %}
```


# 🤝 Contributing

If you’d like to contribute, feel free to submit pull requests. Make sure to follow coding standards and document your changes properly.

# 📜 License

This project is licensed under the MIT License.

# 📬 Contact

For any questions or collaboration opportunities, feel free to reach out!

