# 1. Modell-Liste
curl http://localhost:11434/api/tags

# 2. Gedicht
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Schreibe ein Gedicht über Programmierer."
}'
