from flask import Flask, render_template, request, jsonify, send_file
from ai_generator import generate_product_description
import sqlite3
import os
from datetime import datetime
from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_CENTER



DB_NAME = "database.db"


# -------------------------------
# Create Database
# -------------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        category TEXT,
        brand TEXT,
        price TEXT,
        features TEXT,
        tone TEXT,
        audience TEXT,
        language TEXT,
        seo_title TEXT,
        description TEXT,
        keywords TEXT,
        benefits TEXT,
        cta TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()
app = Flask(__name__)

init_db()


# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# Generate AI Description
# -------------------------------
@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    product_name = data.get("product_name", "")
    category = data.get("category", "")
    brand = data.get("brand", "")
    price = data.get("price", "")
    features = data.get("features", "")
    tone = data.get("tone", "")
    audience = data.get("audience", "")
    language = data.get("language", "")

    result = generate_product_description(
        product_name,
        category,
        brand,
        price,
        features,
        tone,
        audience,
        language,
    )

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO products(
    product_name,
    category,
    brand,
    price,
    features,
    tone,
    audience,
    language,
    seo_title,
    description,
    keywords,
    benefits,
    cta,
    created_at
    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (

        product_name,
        category,
        brand,
        price,
        features,
        tone,
        audience,
        language,
        result["seo_title"],
        result["description"],
        result["keywords"],
        result["benefits"],
        result["cta"],
        datetime.now().strftime("%d-%m-%Y %H:%M")

    ))

    conn.commit()
    conn.close()

    return jsonify(result)


# -------------------------------
# View History
# -------------------------------
@app.route("/history")
def history():

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM products
    ORDER BY id DESC
    """)

    rows = cur.fetchall()

    conn.close()

    data = []

    for row in rows:

        data.append(dict(row))

    return jsonify(data)


# -------------------------------
# Delete History
# -------------------------------
@app.route("/delete/<int:id>")
def delete(id):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("DELETE FROM products WHERE id=?", (id,))

    conn.commit()

    conn.close()

    return jsonify({"message": "Deleted Successfully"})


# -------------------------------
# Download PDF
# -------------------------------
@app.route("/download_pdf", methods=["POST"])
def download_pdf():

    data = request.get_json()

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    style = styles["Heading1"]

    style.alignment = TA_CENTER

    story = []

    story.append(Paragraph("AI Product Description", style))

    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    for key, value in data.items():

        story.append(
            Paragraph(
                f"<b>{key}</b><br/>{value}<br/><br/>",
                styles["BodyText"]
            )
        )

    doc.build(story)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="product_description.pdf",
        mimetype="application/pdf"
    )


# -------------------------------
# Download TXT
# -------------------------------
@app.route("/download_txt", methods=["POST"])
def download_txt():

    data = request.get_json()

    text = ""

    for k, v in data.items():

        text += f"{k}\n"

        text += f"{v}\n\n"

    buffer = BytesIO()

    buffer.write(text.encode())

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="product_description.txt",
        mimetype="text/plain"
    )


# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
