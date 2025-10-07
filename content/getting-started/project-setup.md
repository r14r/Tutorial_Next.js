# Project Setup

Creating a new project is usually as simple as running `npx create-next-app@latest` and answering a few prompts. The generator configures TypeScript, ESLint, and a modern `app/` directory so you can focus on building features rather than scaffolding.

Even without internet access you can mimic the generated structure manually. The important bits include:

1. `package.json` with Next.js, React, and TypeScript dependencies
2. a `next.config.mjs` file so the framework understands how to build the app
3. the `app/` directory containing layouts, routes, and global styles

Once dependencies are installed, run `npm run dev` to launch the development server on [http://localhost:3000](http://localhost:3000).
