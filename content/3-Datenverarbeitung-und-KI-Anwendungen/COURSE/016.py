def extract_entities(text):
    prompt = """Extrahiere Named Entities im JSON-Format:
{
  "Personen": [],
  "Orte": [],
  "Organisationen": []
}
Text: %s""" % text
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(extract_entities("Jeff Bezos gründete Amazon in Seattle."))
