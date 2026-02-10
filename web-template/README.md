<a href="https://precedent.dev">
  <img alt="Precedent – Building blocks for your Next project" src="https://precedent.dev/opengraph-image" />
  <h1 align="center">Precedent</h1>
</a>

<p align="center">
  Building blocks for your Next project
</p>

<p align="center">
  <a href="https://twitter.com/steventey">
    <img src="https://img.shields.io/twitter/follow/steventey?style=flat&label=steventey&logo=twitter&color=0bf&logoColor=fff" alt="Steven Tey Twitter follower count" />
  </a>
  <a href="https://github.com/steven-tey/precedent">
    <img src="https://img.shields.io/github/stars/steven-tey/precedent?label=steven-tey%2Fprecedent" alt="Precedent repo star count" />
  </a>
</p>

<p align="center">
  <a href="#introduction"><strong>Introduction</strong></a> ·
  <a href="#one-click-deploy"><strong>One-click Deploy</strong></a> ·
  <a href="#tech-stack--features"><strong>Tech Stack + Features</strong></a> ·
  <a href="#author"><strong>Author</strong></a>
</p>
<br/>

## Introduction

Precedent is an opinionated collection of components, hooks, and utilities for your Next.js project.

## One-click Deploy



You can also clone & create this repo locally with the following command:

```bash
npx create-next-app precedent --example "https://github.com/steven-tey/precedent"
```

Then, install the dependencies with your package manager of choice:

```bash
npm i
yarn
pnpm i
```

## Tech Stack + Features

https://github.com/user-attachments/assets/aef3c099-e371-43bf-b426-f5ba73185a7c

### Frameworks

- [Next.js](https://nextjs.org/) – React framework for building performant apps with the best developer experience
- [Clerk](https://go.clerk.com/precedent) - A comprehensive user management platform with beautifully designed, drop-in React components

### Platforms


### UI

- [Tailwind CSS](https://tailwindcss.com/) – Utility-first CSS framework for rapid UI development
- [Radix](https://www.radix-ui.com/) – Primitives like modal, popover, etc. to build a stellar user experience
- [Framer Motion](https://framer.com/motion) – Motion library for React to animate components with ease
- [Lucide](https://lucide.dev/) – Beautifully simple, pixel-perfect icons
- [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) – Optimize custom fonts and remove external network requests for improved performance
- [`ImageResponse`](https://nextjs.org/docs/app/api-reference/functions/image-response) – Generate dynamic Open Graph images at the edge

### Hooks and Utilities

- `useIntersectionObserver` –  React hook to observe when an element enters or leaves the viewport
- `useLocalStorage` – Persist data in the browser's local storage
- `useScroll` – React hook to observe scroll position ([example](https://github.com/steven-tey/precedent/blob/main/components/layout/navbar.tsx#L12))
- `nFormatter` – Format numbers with suffixes like `1.2k` or `1.2M`
- `capitalize` – Capitalize the first letter of a string
- `truncate` – Truncate a string to a specified length
- [`use-debounce`](https://www.npmjs.com/package/use-debounce) – Debounce a function call / state update

### Code Quality

- [TypeScript](https://www.typescriptlang.org/) – Static type checker for end-to-end typesafety
- [Prettier](https://prettier.io/) – Opinionated code formatter for consistent code style
- [ESLint](https://eslint.org/) – Pluggable linter for Next.js and TypeScript

### Miscellaneous


## Author

- Steven Tey ([@steventey](https://twitter.com/steventey))
