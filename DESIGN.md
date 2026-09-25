---
name: Abisanka GitHub Profile
description: Theme-aware original SVG artwork for a GitHub-native AI engineering profile.
colors:
  light-field: "#e8edff"
  light-ink: "#172b78"
  light-muted: "#3c5093"
  light-mesh: "#4b68b7"
  light-signal: "#af4936"
  light-panel: "#f9fbff"
  dark-field: "#101b36"
  dark-ink: "#f2f5ff"
  dark-muted: "#b2c8ef"
  dark-mesh: "#80a9ef"
  dark-signal: "#ffab90"
  dark-panel: "#18284b"
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
    fontSize: "28px"
    fontWeight: 700
rounded:
  artwork: "14px"
  calendar: "12px"
  calendar-day: "3px"
components:
  hero-light:
    backgroundColor: "{colors.light-field}"
    textColor: "{colors.light-ink}"
    rounded: "{rounded.artwork}"
  hero-dark:
    backgroundColor: "{colors.dark-field}"
    textColor: "{colors.dark-ink}"
    rounded: "{rounded.artwork}"
  project-light:
    backgroundColor: "{colors.light-panel}"
    textColor: "{colors.light-ink}"
    rounded: "{rounded.artwork}"
  project-dark:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.dark-ink}"
    rounded: "{rounded.artwork}"
  activity-light:
    backgroundColor: "{colors.light-field}"
    textColor: "{colors.light-ink}"
    rounded: "{rounded.calendar}"
  activity-dark:
    backgroundColor: "{colors.dark-field}"
    textColor: "{colors.dark-ink}"
    rounded: "{rounded.calendar}"
---

# Design System: Abisanka GitHub Profile

## Overview

An original orbital wire sculpture and warm signal line frame Abisanka's engineering work. High-contrast light and dark SVG palettes support GitHub's appearance settings. The README is a native GitHub document: artwork introduces sections, while project explanations and links remain selectable content.

## Colors

The light palette uses a pale blue field with deep blue ink; the dark palette uses a navy field with near-white ink. Each has its own muted text, mesh, panel, and coral signal colors. The activity chart uses separate five-step light and dark intensity ramps; the legend indicates contribution frequency.

## Typography

Artwork uses Trebuchet MS with Segoe UI and Arial fallbacks. The desktop hero name uses 79- and 65-unit lines, with a 34-unit statement. Mobile uses 60- and 49-unit name lines, a 30-unit statement, and 20-unit stacked discipline labels. The calendar uses the system sans-serif stack. GitHub controls the Markdown body type and native link presentation.

## Layout

The README runs from linked hero through contact links, introduction, current work, selected projects, visual toolkit, activity, and contact. Four linked project illustrations form a two-column table, followed by selectable descriptions and links. Four linked toolkit cards form a second two-column table. Additional experiments sit in a native details disclosure.

README picture elements choose light/dark artwork through prefers-color-scheme. At 600px and below, hero and activity switch to separate mobile compositions. The hero is 960 × 408 desktop and 560 × 490 mobile. Project icons are 320 × 174; the footer is 960 × 100.

The desktop activity drawing is 960 × 320 and shows the returned annual calendar with 15-unit day cells at 17-unit steps. Mobile is 390 × 355 and shows the latest 18 weeks with 16-unit cells at 19-unit steps. Both label the annual total, visible date range, legend, source, and update date. A second 960 × 290 desktop / 390 × 355 mobile drawing shows active days, longest run, peak month, and monthly contribution bars.

## Elevation & Depth

There are no shadows. Flat fields, fine mesh intersections, and the coral trajectory create visual depth. The sculpture is decorative, not a model diagram or performance measure.

## Shapes

Artwork panels use rounded corners. Fine connected lines form the orbital mesh and project-specific diagrams; calendar days are small rounded squares. The footer repeats the signal color in a simple arrow.

## Components

**Hero:** The four hero-light/dark and hero-mobile-light/dark SVGs have paired theme palettes and separate desktop/mobile compositions. The full hero image links to selected work. A highlight travels along the orbit once over 4.5 seconds; reduced-motion preference disables it.

**Projects, toolkit, and footer:** The Autograd, OpenOrbit, Holo-Vex, and FacPosCheck icons each have light/dark SVGs (project-autograd, project-orbit, project-holo, and project-vision) and link to their repositories. Four linked toolkit cards depict model computation, agent connections, visual sensing, and application delivery. Footer-light.svg and footer-dark.svg carry the closing line and link to email.

**Activity:** Four local activity SVGs pair desktop/mobile with light/dark themes. Four momentum SVGs provide the monthly view and compact summary. Both images link to GitHub's native interactive contribution calendar, where visitors can inspect individual days. A weekly workflow refreshes the static images from GitHub data. The images include SVG titles/descriptions and README alternative text.

## Do's and Don'ts

- **Do** keep light/dark asset pairs, the separate mobile compositions, and meaningful text alternatives together.
- **Do** keep project images linked and descriptions as native Markdown; keep the activity image linked to GitHub's interactive graph.
- **Do** preserve the finite hero motion and reduced-motion rule when rebuilding artwork.
- **Don't** present contribution intensity or decorative geometry as evidence of engineering quality.
