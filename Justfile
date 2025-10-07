set shell := ["sh", "-eu", "-c"]

# Install project dependencies
install:
	npm install

# Build the production bundle
build:
	npm run build

# Start the development server
run:
	npm run dev

# Generate static pages into the out directory
create-static-pages:
	npm run build
	npx next export

# Serve the previously generated static site
show-static-site:
	npx serve out
