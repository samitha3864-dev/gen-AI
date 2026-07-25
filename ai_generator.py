import random

def generate_product_description(
    product_name,
    category,
    brand,
    price,
    features,
    tone,
    audience,
    language,
):

    intros = [
        f"Introducing the all-new {product_name} from {brand}.",
        f"Experience premium quality with the {brand} {product_name}.",
        f"Upgrade your lifestyle with the {product_name}.",
        f"Discover the latest {category} from {brand}.",
    ]

    benefits = [
        "Premium Quality",
        "Stylish Design",
        "Reliable Performance",
        "Easy to Use",
        "Long-lasting Durability",
    ]

    description = f"""
{random.choice(intros)}

The {product_name} is a high-quality {category} specially designed for {audience.lower()}.

Product Features:
{features}

Why Choose This Product?

• Premium Build Quality

• Excellent Performance

• Affordable Price

• Attractive Design

Brand:
{brand}

Price:
{price}

This product combines innovation, style, and reliability to provide an outstanding user experience.
"""

    seo_title = f"{brand} {product_name} | Best {category} Online"

    keywords = f"""
{product_name},
{brand},
{category},
Best {category},
Affordable {category},
Premium {category},
Buy {product_name},
Online Shopping
"""

    cta = "🛒 Order now and enjoy premium quality with the best value for your money!"

    return {
        "seo_title": seo_title,
        "description": description,
        "benefits": "\n".join(f"✔ {b}" for b in benefits),
        "keywords": keywords,
        "cta": cta,
    }