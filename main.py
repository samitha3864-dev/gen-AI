from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    return send_from_directory("static", "product.html")


@app.route("/api/generate", methods=["POST"])
def generate():

    data = request.get_json()

    name = data.get("productName", "").strip()
    category = data.get("productCategory", "").strip()
    features = data.get("productFeatures", "").strip()

    if not name or not category:
        return jsonify({
            "output": "Please enter Product Name and Category."
        })

    feature_list = []

    if features:
        feature_list = [f.strip() for f in features.split(",") if f.strip()]
    else:
        feature_list = [
            "Premium Quality",
            "Easy to Use",
            "Long Lasting"
        ]

    feature_text = "\n".join([f"• {item}" for item in feature_list])

    description = f"""
📦 PRODUCT TITLE
{name}

📝 PRODUCT DESCRIPTION

The {name} is a premium {category.lower()} product designed to deliver excellent performance, durability, and reliability. It combines modern design with advanced functionality, making it an ideal choice for everyday use. Whether for personal or professional purposes, {name} offers outstanding quality and value.

⭐ KEY FEATURES

{feature_text}

• Premium Build Quality
• User-Friendly Design
• Reliable Performance

🎯 BENEFITS

• High Performance
• Durable and Reliable
• Easy to Operate
• Excellent Value for Money
• Suitable for Daily Use

🔍 SEO KEYWORDS

{name}, {category}, Best {category}, Premium {category}, Buy {name} Online

💡 MARKETING TAGLINE

"Experience Quality. Experience {name}."

⭐ WHY CHOOSE THIS PRODUCT?

The {name} is designed for customers who value quality, performance, and affordability. It offers a perfect balance of innovation, style, and reliability.

Thank you for choosing {name}!
"""

    return jsonify({
        "output": description
    })


if __name__ == "__main__":
    app.run(debug=True)