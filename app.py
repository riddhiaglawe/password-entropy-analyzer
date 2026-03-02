from flask import Flask, render_template, request, jsonify, send_file
import math
import re
import random
import string
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import io

app = Flask(__name__)

def calculate_entropy(password):
    length = len(password)
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    return round(length * math.log2(charset), 2)


def password_strength(entropy):
    if entropy < 28:
        return "Very Weak", "#d93025"
    elif entropy < 36:
        return "Weak", "#f9ab00"
    elif entropy < 60:
        return "Moderate", "#fbbc04"
    elif entropy < 128:
        return "Strong", "#34a853"
    else:
        return "Very Strong", "#0f9d58"


def generate_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length (minimum 8 characters).")

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters (A–Z).")

    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters (a–z).")

    if not re.search(r"[0-9]", password):
        suggestions.append("Add numbers (0–9).")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Add special symbols (!@#$%^&*).")

    return suggestions


def crack_time(entropy):
    guesses_per_second = 10_000_000_000
    seconds = (2 ** entropy) / guesses_per_second
    years = seconds / 31536000
    return round(years, 2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    password = data.get("password", "")

    entropy = calculate_entropy(password)
    strength, color = password_strength(entropy)
    suggestions = generate_suggestions(password)
    years = crack_time(entropy)
    meter_width = min((entropy / 128) * 100, 100)

    return jsonify({
        "entropy": entropy,
        "strength": strength,
        "color": color,
        "years": years,
        "suggestions": suggestions,
        "meter_width": meter_width
    })


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    length = int(data.get("length", 12))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return jsonify({"password": password})


@app.route("/generate_report", methods=["POST"])
def generate_report():
    data = request.get_json()
    password = data.get("password", "")

    entropy = calculate_entropy(password)
    strength, _ = password_strength(entropy)
    years = crack_time(entropy)

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Password Forensic Analysis Report", styles["Heading1"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Entropy: {entropy} bits", styles["Normal"]))
    elements.append(Paragraph(f"Strength: {strength}", styles["Normal"]))
    elements.append(Paragraph(f"Estimated Crack Time: {years} years", styles["Normal"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Attack Comparison:", styles["Heading2"]))
    elements.append(Paragraph("• Online Attack (~1,000 attempts/sec)", styles["Normal"]))
    elements.append(Paragraph("• GPU Offline Attack (~10 Billion/sec)", styles["Normal"]))
    elements.append(Paragraph("• Distributed Botnet (~1 Trillion/sec)", styles["Normal"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Forensic Feasibility Conclusion:", styles["Heading2"]))
    elements.append(Paragraph(
        "Based on entropy and simulated attack models, brute-force recovery feasibility has been evaluated.",
        styles["Normal"]
    ))

    doc.build(elements)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="Forensic_Report.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)