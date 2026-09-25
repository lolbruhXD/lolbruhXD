---
name: Abisanka GitHub Profile
description: Original cobalt and coral artwork for a GitHub-native AI engineering profile.
colors:
  cobalt: "#234cdf"
  coral: "#ffac95"
  warm-white: "#fff8ed"
  wire-blue: "#a4baff"
  pale-surface: "#eef2ff"
  work-accent: "#bd5c43"
  work-divider: "#bdc9ed"
  calendar-light-text: "#172340"
  calendar-light-muted: "#485979"
  calendar-dark-surface: "#121b2b"
  calendar-dark-text: "#f1f4ff"
  calendar-dark-muted: "#a9bbd5"
typography:
  display:
    fontFamily: "Trebuchet MS, Segoe UI, Arial, sans-serif"
    fontSize: "79px"
    fontWeight: 700
    letterSpacing: "-2.5px"
  headline:
    fontFamily: "Trebuchet MS, Segoe UI, Arial, sans-serif"
    fontSize: "34px"
    fontWeight: 700
  calendar-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif"
    fontSize: "25px"
    fontWeight: 700
rounded:
  hero: "14px"
  artwork: "10px"
  calendar: "12px"
  day: "2px"
components:
  hero:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.hero}"
  work-strip:
    backgroundColor: "{colors.pale-surface}"
    rounded: "{rounded.artwork}"
  calendar-light:
    backgroundColor: "{colors.pale-surface}"
    textColor: "{colors.calendar-light-text}"
    rounded: "{rounded.calendar}"
  calendar-dark:
    backgroundColor: "{colors.calendar-dark-surface}"
    textColor: "{colors.calendar-dark-text}"
    rounded: "{rounded.calendar}"
---

# Design System: Abisanka GitHub Profile

## Overview

Original orbital wire sculpture pairs a bold cobalt field with a coral trajectory. The visual identity supports Abisanka's AI engineering work, while résumé-grounded prose and verified public project links carry the evidence.

This is a GitHub profile README, not a custom website. Local, self-contained SVG artwork frames native Markdown content. The identity is direct, technical, and personal; no external badges, image services, or downloaded fonts are needed.

## Colors

Cobalt anchors the hero and footer. Coral traces the orbital path and bottom rule; warm white carries their prominent text. Wire blue makes the fine sculpture lines visible without competing with the name.

The work strip uses a pale surface, cobalt diagrams, muted dividers, and a deeper coral accent. The calendar has separate light and dark surfaces and text colors. Its ordered five-step intensity ramps run from a quiet neutral through violet to warm coral; the legend communicates relative activity, not engineering quality.

## Typography

The artwork uses the local Trebuchet MS / Segoe UI / Arial stack. The frontmatter records desktop SVG coordinate sizes, which scale with each image. The desktop name uses two lines at 79 and 65 units; the statement uses 34. The mobile drawing uses name lines at 60 and 49, a statement at 30, and stacked discipline labels at 20.

Calendar text uses the system sans-serif stack. GitHub controls Markdown body type, headings, inline code, tables, links, and disclosure controls; do not attempt to override them with page CSS.

## Layout

The README is a single native document column: hero, contact links, introduction, current work, selected projects, tools, activity, and contact. Longer experiments use a native `details` disclosure. Project descriptions and links remain selectable Markdown instead of being baked into images.

All artwork uses a responsive full-width image. The hero has separate desktop (960 × 408) and mobile (560 × 490) compositions. A `picture` source switches at a maximum viewport width of 600px. Mobile rearranges the name, statement, disciplines, and sculpture rather than shrinking the desktop composition.

The calendar uses the same breakpoint: desktop (960 × 306) shows the returned year; mobile (560 × 332) shows the latest 26 weeks. Desktop day cells are 12 units with a 16-unit step; mobile cells are 14 with a 19-unit step. Its annual total remains explicitly labeled even in the shorter mobile view. The work strip and footer scale from 960-unit-wide drawings.

## Elevation & Depth

There are no shadows. Flat color fields, fine wire intersections, and the coral orbital trajectory create the visual depth. The sculpture is decorative geometry, not a scientific result or performance chart.

## Shapes

Large image panels have gently rounded corners. The repeated language is linework: connected nodes, stacked documents, intersecting orbits, a pose figure, and a simple footer arrow. Calendar days are small rounded squares. Keep illustration detail subordinate to readable text.

## Components

**Hero:** `assets/hero.svg` and `assets/hero-mobile.svg` contain the same identity and statement with independent compositions. A small light signal travels along the coral path once over 4.5 seconds with `ease-in-out`; `prefers-reduced-motion: reduce` disables the animation. The resting image remains complete and understandable.

**Work strip and footer:** `assets/work.svg` introduces four disciplines with original diagrams. `assets/footer.svg` repeats the cobalt/coral identity and the closing statement. Both are static.

**Activity calendar:** four local `activity-*.svg` variants combine desktop/mobile with light/dark presentation. README `picture` sources select the appropriate size and `prefers-color-scheme` variant. Each drawing includes dates, an annual contribution total, a Less–More legend, the GitHub source, and an update date. A weekly workflow refreshes the data. Images have SVG titles/descriptions and README alternative text.

**Native content:** ordinary Markdown headings, project links, inline technology labels, a toolkit table, and the disclosure provide the reading structure. Interactive appearance, focus, hover, and keyboard behavior belong to GitHub.

## Do's and Don'ts

- **Do** preserve local SVG assets, meaningful alternative text, and native Markdown project descriptions.
- **Do** retain the mobile compositions, both calendar themes, finite motion, and reduced-motion rule when rebuilding artwork.
- **Do** keep the profile grounded in the résumé and verified public links; label additional work without inventing repository URLs.
- **Don't** substitute external badge walls or third-party image widgets for the original identity.
- **Don't** introduce custom website navigation, scripts, remote fonts, or README styling that depends on unsupported CSS.
- **Don't** describe contribution intensity or the orbital illustration as evidence of performance or model quality.
