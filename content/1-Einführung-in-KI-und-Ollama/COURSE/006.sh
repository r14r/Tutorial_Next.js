# 1. Gesundheitscheck
curl http://localhost:11434

# 2. Einfacher Chat mit llama2
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Nenne drei Programmiersprachen"
}'
