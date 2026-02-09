# Enterprise Standard: Bluesky Professional Marketing Protocol

Status: **MANDATORY**
Last Update: 2026-02-09

All affiliate marketing and external linking on Bluesky must follow this high-conversion standard.

## 1. Primary Method: Link Cards (External Embeds)
Every affiliate post must implement a clickable **Link Card**.
- **Visuals**: Primary 4K thumbnail (Realistic, Cinematic).
- **Title**: Compelling, benefit-oriented (e.g., "Luxury Private Jet Charter").
- **Description**: Clear value proposition (EEA-T compliant text).

## 2. Standard: Clean Text Flow
The post body should remain clean and professional, focusing on the elite experience. All calls-to-action are handled by the **Link Card**.
- **NO duplicate links**: Do not include "Book Now" or URLs in the text.
- **Visual Focus**: The image and card serve as the sole gateway to the affiliate partner.

## 3. Implementation (Python Reference)
```python
client.post_with_link_card(
    text=rich_text, 
    url="https://villiers.ai/?id=11089",
    title="Luxury Private Jet Charter | Book in 2026",
    description="Peak aviation excellence. Real-time availability, global reach.",
    thumb_path=image_path,
    facets=facets
)
```

---
*Authorized by Jules AI for TravelKing.Live Enterprise.*
