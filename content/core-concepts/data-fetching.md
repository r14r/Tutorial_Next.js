# Data Fetching Patterns

Next.js simplifies data requirements with Route Handlers, Server Actions, and `fetch` caching. Consider the following guidelines when planning your data layer:

- Fetch data in server components whenever possible to keep bundles small.
- Opt into caching by default, or mark fetches as `cache: "no-store"` when you need the freshest data.
- Use loading UI (`loading.tsx`) to provide immediate feedback for slow requests.

Combining these patterns with MDX-powered content helps you ship fast documentation sites and dashboards alike.
