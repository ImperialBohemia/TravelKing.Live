# 🏆 OMEGA Next.js Gold Standard (2026.MAX)

This document defines the absolute best practices for web development at TravelKing.Live, synthesized from official Next.js documentation and Google's Developer Standards.

## 🚀 1. Core Performance (Google Core Web Vitals)
- **LCP (Largest Contentful Paint)**: Keep under 2.5s. Use `next/image` for all assets.
- **FID (First Input Delay)**: Keep under 100ms. Minimize main-thread work.
- **CLS (Cumulative Layout Shift)**: Keep under 0.1. Always specify dimensions for images.

## 🏗️ 2. Architectural Purity (App Router)
- **Server Components (RSC)**: Default to Server Components. Use Client Components (`'use client'`) only for interactivity (hooks, event listeners).
- **Streaming & Suspense**: Use `loading.tsx` and `Suspense` for granular loading states to improve perceived speed.
- **Parallel Routes**: Use `@folder` patterns for dashboards to render multiple pages in the same layout simultaneously.

## 🔍 3. Advanced SEO & AEO (AI Optimization)
- **Metadata API**: Always export `metadata` or `generateMetadata` from `page.tsx` or `layout.tsx`.
- **JSON-LD**: Inject schema.org structured data to help AI agents (Gemini, GPT) understand the content hierarchy.
- **OpenGraph**: Provide high-quality `opengraph-image.tsx` for every dynamic route.

## 👁️ 4. Mobile-First Excellence
- All components must be verified in the **OMEGA Visual Eye (Mobile Mode)**.
- Use Tailwind's `sm:`, `md:`, `lg:` prefixes to ensure fluid responsiveness.

## 🧪 5. Zero-Failure Testing
- Every new component MUST have a corresponding `.test.tsx` file.
- Deployment is strictly blocked if `npm run test` or `bash testing-lab/run_audit.sh` fails.

---
*Inspired by Google Developers and Vercel Best Practices.*

## 🌍 6. "Best on Planet" Mandates
- **Zero CLS**: Every layout shift is an error.
- **Instant Hydration**: Client components must be leaf nodes wherever possible.
- **AEO-First**: Content is structured for machines first, humans second.
- **Atomic Reliability**: Every component has a test; every test passes.
