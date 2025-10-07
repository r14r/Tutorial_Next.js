# Next.js Tutorial Starter

This project is a custom scaffolded Next.js application that mirrors the output of `create-next-app` while adding a documentation-style layout:

- Chapter navigation in the header
- Subchapter navigation in a sticky sidebar
- Content sourced from Markdown (`.md`) and MDX (`.mdx`) files

## Getting Started

1. Install dependencies
   ```bash
   npm install
   ```
2. Run the development server
   ```bash
   npm run dev
   ```
3. Open [http://localhost:3000](http://localhost:3000) to view the tutorial.

The home route redirects to the first available chapter. Update the entries in `lib/chapters.ts` and add new files in the `content/` directory to expand the curriculum.
