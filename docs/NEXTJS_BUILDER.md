# 🛠️ OMEGA Next.js Builder Protocol

This document defines the **Elite OMEGA Standard** for all web development within this project. No modifications to the web platform should be made without adhering to this registry.

## 🏗️ Core Registry

| Component | Path | Purpose |
| :--- | :--- | :--- |
| **Hero** | `web-latest/src/components/sections/HeroSection.tsx` | Core value prop & status. |
| **Search** | `web-latest/src/components/sections/SearchSection.tsx` | Global data scanning. |
| **Features** | `web-latest/src/components/sections/FeaturesSection.tsx` | System capabilities grid. |
| **WorldMap** | `web-latest/src/components/sections/MapSection.tsx` | Global network visualization. |
| **Pricing** | `web-latest/src/components/sections/PricingSection.tsx` | Access tiers & conversion. |
| **CTA** | `web-latest/src/components/sections/CTASection.tsx` | Final conversion point. |
| **Navbar** | `web-latest/src/components/Navbar.tsx` | Global navigation. |
| **Footer** | `web-latest/src/components/Footer/index.tsx` | Legal & compliance. |
| **Blog** | `web-latest/src/components/sections/BlogSection.tsx` | Elite travel blog feed. |

## 📐 Best Practices (Mandatory)

1.  **Instant Identification**: When asked to change a part of the site, refer to the table above to find the exact file immediately.
2.  **Sectional Purity**: Each major section of the landing page must reside in its own file within `web-latest/src/components/sections/`.
3.  **Theming**: Strictly use Tailwind's `primary`, `secondary`, and `accent` tokens. No hardcoded hex values in component logic.
4.  **Performance**: Use `framer-motion` for entry animations to maintain the "Elite/High-Tech" aesthetic.
5.  **Clean Code**: Maintain `use client` only where interactive hooks or animations are required.

---
*Authorized by: OMEGA Intelligence Hub*
