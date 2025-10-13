set shell := ["sh", "-eu", "-c"]

# Show help when running `just` without arguments
default: help

# Display available commands
help:
	@echo "Available tasks:"
	@echo "  install              Install project dependencies"
	@echo "  build                Build the production bundle"
	@echo "  run                  Start the development server"
	@echo "  create-static-pages  Build and export a static site"
	@echo "  show-static-site     Serve the exported static site"
	@echo "  translate            Translate markdown between locales"
	@echo
	@echo "Translate usage:"
	@echo "  just translate [--from <src>] [--to <dest>] [--content <path>] [--dry-run] [--overwrite]"
	@echo "  Example dry run: just translate --dry-run"
	@echo "  Example overwrite: just translate --from de --to en --overwrite"

# Install project dependencies
install:
	pnpm install

# Build the production bundle
build:
	pnpm run build

# Start the development server
run:
	pnpm run dev

# Generate static pages into the out directory
create-static-pages:
	pnpm run build
	npx next export

# Serve the previously generated static site
show-static-site:
	npx serve out


# Translate markdown content between locales
translate *args:
	pnpm run translate -- --from de --to en --content content {{args}}
