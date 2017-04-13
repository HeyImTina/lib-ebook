from flask import request, jsonify

from app.model import db
from app.model.ebook import Ebook
from . import api


@api.route("/ebook/edit", methods=['POST'])
def ebook_edit():
    ret = Ebook.query.filter_by(id=request.form.get("id")).first()
    if ret:
        ret.title = request.form.get("title")
        ret.author = request.form.get("author")
        ret.chapter = request.form.get("chapter")
        ret.text = request.form.get("text")
        db.session.commit()
    return jsonify({
        "code": 0,
        "msg": "ok"
    })


@api.route("/ebook/add", methods=['POST'])
def ebook_add():
    db.session.add(Ebook(
        title=request.form.get("title"),
        author=request.form.get("author"),
        chapter=request.form.get("chapter"),
        text=request.form.get("text")
    ))
    try:
        db.session.commit()
        return jsonify({
            "code": 0,
            "msg": "ok"
        })
    except:
        return jsonify({
            "code": 1,
            "msg": "error"
        })


@api.route("/ebook/list")
def ebook_list():
    search = request.args.get("search", None)
    page = request.args.get("page", 1)
    num = request.args.get("num", 10)
    if search:
        ret = Ebook.query.filter(Ebook.title.like("%" + search + "%")).offset((page - 1) * num).limit(num).all()
    else:
        ret = Ebook.query.offset((page - 1) * num).limit(num).all()
    data = [x.json() for x in ret]
    return jsonify({
        "code": 0,
        "data": data
    })


@api.route("/ebook/<int:book_id>")
def ebook(book_id):
    ret = Ebook.query.filter_by(id=book_id).first()
    if ret:
        return jsonify({
            "code": 0,
            "data": ret.json()
        })
    else:
        return jsonify({
            "code": 1,
            "msg": "not found!"
        })


