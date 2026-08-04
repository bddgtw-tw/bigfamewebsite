"""Normalize high-priority English metadata without changing page body claims."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
UPDATES = {
    "en/index.html": (
        "Taiwan-based B2B sourcing and export coordination for retail display fixtures, display hardware, POS displays and custom metal components. Big Fame connects overseas clients with suitable Taiwan manufacturers.",
        "Taiwan B2B sourcing for retail display fixtures, display hardware, POS displays and custom metal parts. Big Fame connects overseas buyers with Taiwan manufacturers.",
    ),
    "en/applications.html": (
        "Explore anonymous project selections and real spatial applications, from retail fixtures to hospitality furniture, with Taiwan sourcing and export coordination by Big Fame.",
        "Explore anonymous Big Fame project selections, from retail fixtures to hospitality furniture, with Taiwan sourcing and export coordination.",
    ),
    "en/services.html": (
        "Discover Big Fame's turn-key B2B service integration, including requirement scoping, value engineering, precision prototyping, project-based inspection coordination, and international sea/air logistics.",
        "Big Fame B2B service integration: requirement scoping, value engineering, prototyping, inspection coordination and international logistics.",
    ),
    "en/anti-theft-hooks.html": (
        "Sourcing entry for anti-theft display hooks. Start with product security, handling flow, display system and site conditions; confirm final specifications by SKU, drawing and sample.",
        "Anti-theft display hook sourcing entry. Compare security, handling flow and display systems, then confirm specifications by SKU, drawing and sample.",
    ),
    "en/anti-theft-hooks/index.html": (
        "Sourcing entry for anti-theft display hooks. Start with product security, handling flow, display system and site conditions; confirm final specifications by SKU, drawing and sample.",
        "Anti-theft display hook sourcing entry. Compare security, handling flow and display systems, then confirm specifications by SKU, drawing and sample.",
    ),
    "en/case-page-cosmetic-organizer.html": (
        "An evidence-controlled PAGE tabletop cosmetic organizer record: dimensions, acrylic and solid wood materials, packing and sample or bulk lead-time notes from the 2020-03-30 ver.01 document.",
        "Evidence-controlled PAGE tabletop cosmetic organizer record with dimensions, acrylic, solid wood, packing and documented lead-time notes.",
    ),
    "en/technical-resources.html": (
        "Technical resources, dimension evidence and CAD request entry for retail display equipment. Start with verified evidence, then confirm formal files by SKU, drawing and sample.",
        "Technical resources and CAD request entry for retail display equipment. Start with evidence, then confirm files by SKU, drawing and sample.",
    ),
}

for rel, (old, new) in UPDATES.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new, 1)
    elif new in text:
        continue
    else:
        raise SystemExit(f"Metadata value not found in {rel}")
    path.write_text(text, encoding="utf-8")
print(f"Updated {len(UPDATES)} English metadata descriptions.")
