
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "todo.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    deadline = db.Column(db.String(20))

    def mark_done(self):
        self.done = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if title:
            db.session.add(Task(title=title))
            db.session.commit()

        return redirect(url_for("index"))

    tasks = db.session.scalars(
        db.select(Task).order_by(Task.id)
    ).all()

    return render_template("index.html", tasks=tasks)


@app.route("/done/<int:task_id>", methods=["POST"])
def done(task_id):
    task = db.get_or_404(Task, task_id)
    task.mark_done()
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = db.get_or_404(Task, task_id)
    if request.method == "POST":
        task.title = request.form["title"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", task=task)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
