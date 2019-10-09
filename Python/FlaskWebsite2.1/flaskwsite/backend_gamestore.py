from flaskwsite import db
from flaskwsite.models import Game
from sqlalchemy import exc
from flask import flash, render_template


class Backend(object):

    def __init__(self, form):
        self.form = form
        self.form.table.choices = []
        self.game = Game

    def search_entry(self):
        searched_games = self.game.query.filter(
            (self.game.title == self.form.title.data) | (self.game.company == self.form.company.data)
            | (self.game.type == self.form.type.data)
            | (self.game.rdate == self.form.rdate.data)).all()
        game_list = [(i.id, ', '.join((i.title, i.company, i.type, i.rdate))) for i in searched_games]

        if len(game_list) == 0:
            flash('Record not found.', 'danger')
            return render_template("gamestore.html", form=self.form)
        else:
            self.form.table.choices = game_list
            return render_template("gamestore.html", form=self.form)

    def find_by_id(self, id):
        return Game.query.filter(Game.id == id).all()

    def print_all(self):
        if len(Game.query.all()) == 0:
            flash('Store is empty!', 'danger')
            return render_template("gamestore.html", form=self.form)
        else:
            game_list = [(i.id, ', '.join((i.title, i.company, i.type, i.rdate))) for i in Game.query.all()]
            self.form.table.choices = game_list
            return render_template("gamestore.html", form=self.form)

    def add_entry(self):
        try:
            game = Game(title=self.form.title.data, company=self.form.company.data, type=self.form.type.data,
                        rdate=self.form.rdate.data)
            db.session.add(game)
            db.session.commit()
            flash(f'{self.form.title.data} - Game added!', 'success')
            return self.print_all()

        except exc.IntegrityError:
            flash(f'{self.form.title.data} - you have this game!', 'danger')
            return render_template("gamestore.html", form=self.form)

    def delete_all(self):
        if len(Game.query.all()) == 0:
            flash('Store is empty!', 'danger')
            return render_template("gamestore.html", form=self.form)
        else:
            db.drop_all()
            db.create_all()
            flash(f'All games deleted!', 'danger')
            return render_template("gamestore.html", form=self.form)

    def delete_selected(self):
        try:
            index = int(self.form.table.data[0])

            game = self.find_by_id(index)

            db.session.delete(game[0])
            db.session.commit()

            return self.print_all()
        except IndexError:
            flash('No objects to delete!', 'danger')
            return render_template("gamestore.html", form=self.form)

    def update_selected(self):
        try:
            index = int(self.form.table.data[0])

            update_this = Game.query.filter_by(id=index).first()
            update_this.title = self.form.title.data
            update_this.company = self.form.company.data
            update_this.type = self.form.type.data
            update_this.rdate = self.form.rdate.data

            db.session.commit()
            flash(f'{self.form.title.data} - Record updated!', 'success')
            return self.print_all()
        except IndexError:
            flash('Nothing to update!', 'danger')
            return render_template("gamestore.html", form=self.form)
