
# Refactored: Read profile data from JSON (ask.json or poorni.json)
import os
import json
import sys
from docx import Document
from docx2pdf import convert

def load_profile_data(profile_json=None):
    if profile_json is None:
        profile_json = os.environ.get("PROFILE_JSON")
        if profile_json is None:
            raise ValueError("Profile JSON file name must be provided as a parameter or via the PROFILE_JSON environment variable.")
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    json_path = os.path.join(data_dir, profile_json)
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Profile JSON file not found: {json_path}")
    with open(json_path, "r") as f:
        profile = json.load(f)
    return profile

profile_json = sys.argv[1] if len(sys.argv) > 1 else None
# Usage: pass the file name as a parameter or set PROFILE_JSON env variable
profile = load_profile_data(profile_json)
doc = Document()

# Name and Contact

doc.add_heading(profile["name"], level=1)
contact = profile.get("contact", {})
city = contact.get("city", "")
state = contact.get("state", "")
mobile = contact.get("mobileNumber", "")
doc.add_paragraph(f"{city}, {state} | {mobile}")
# Social links
social_lines = []
for s in profile.get("social", []):
    for k, v in s.items():
        social_lines.append(f"{v.get('name')}: {v.get('url')}")
for o in profile.get("other", []):
    for k, v in o.items():
        social_lines.append(f"{v.get('name')}: {v.get('url')}")
for line in social_lines:
    doc.add_paragraph(line)
# Summary
summary = profile.get("profileSummary", {})
doc.add_heading(summary.get("title", "Professional Summary"), level=2)
doc.add_paragraph(summary.get("content", ""))
# Skills
doc.add_heading("Skills", level=2)
for skill in profile.get("skills", []):
    para = doc.add_paragraph()
    run_title = para.add_run(f"{skill['title']}:")
    run_title.bold = True
    para.add_run(f" {skill['text']}")
# Experience
doc.add_heading("Professional Experience", level=2)
for exp in profile.get("experiences", []):
    doc.add_heading(f"{exp['title']} – {exp['company']}", level=3)
    doc.add_paragraph(f"{exp['location']} | {exp['dates']}")
    for bullet in exp.get("bullets", []):
        doc.add_paragraph(bullet, style="List Bullet")
# Education & Certifications
doc.add_heading("Education & Certifications", level=2)
doc.add_paragraph("Bachelor of Engineering – Computer Science, Anna University")
doc.add_paragraph("AWS Certified Solutions Architect – Associate")
file_path = f"./{profile['name']}_Resume.docx"


doc.save(file_path)
print("Convert to PDF")
convert(file_path)