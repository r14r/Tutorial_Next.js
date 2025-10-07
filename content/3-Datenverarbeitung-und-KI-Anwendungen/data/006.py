text = "Die Regierung hat ein neues Gesetz verabschiedet."
prompt = f"""Klassifiziere den Text und antworte im JSON-Format:
{{
  "Text": "{text}",
  "Thema": "<Kategorie>"
}}
"""
