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

## Localizing content

UI strings are translated with [`next-intl`](https://next-intl-docs.vercel.app/), and the markdown syllabus now lives under locale-aware directories. Each locale gets its own tree inside `content/<locale>/`, mirroring the chapter structure defined in `lib/chapters.ts`.

To add or translate a lesson:

1. Create a locale folder if it does not yet exist, e.g. `content/en/`.
2. Mirror the chapter path: `content/en/day-1/content.md`, `content/en/day-1/1-1.md`, …
3. Add translated markdown files. Anything missing automatically falls back to the default locale (`content/de/...`) and finally to the legacy shared files in `content/<chapter>/`.

The loader first checks `content/<current-locale>/…`, then `content/<default-locale>/…`, and finally the historical root locations. That means you can migrate gradually—mixing translated and untranslated chapters without breaking navigation.

## Batch translations with Ollama

If you have [Ollama](https://ollama.com/) running locally (the default server listens on `http://localhost:11434`), you can auto-translate an entire locale tree with:

```bash
pnpm run translate -- --from de --to en --content content
```

- `--from` (`de` in the example) points to the source locale directory inside `content/`.
- `--to` is the target locale; files are written to `content/<to>/…` mirroring the original structure.
- `--content` can target a different root if you keep content elsewhere.
- Add `--dry-run` to preview work without writing files, or `--overwrite` to replace existing translations.
- Use `--model llama3` (default) or any other locally available model.

Non-markdown files are copied verbatim, while `.md`/`.mdx` files are translated. Missing chapters fall back to the default locale at runtime, so you can translate incrementally chapter by chapter.
