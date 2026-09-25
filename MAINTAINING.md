# Maintaining this profile

The public profile is the root `README.md` in `lolbruhXD/lolbruhXD`.
GitHub displays it on the account profile when this repository is public.

## Content

Edit the README to update experience, project descriptions, dates, or links.
Current professional information comes from the résumé supplied on 25 September 2026.
Public project descriptions were checked against the corresponding repositories.
The source résumé itself is not included here.

The additional experiments section contains résumé projects without public source links.
The public `Creating-Make-More` repository was not featured because its default branch
contained only a README when reviewed. Autograd is presented as a learning implementation,
and FacPosCheck as an experiment; neither is described as a validated production system.

## Artwork

All images are repository-local SVGs. No analytics pixels, visitor counters, external
font requests, or third-party badge servers are used. The orbital wire sculpture is
original decorative artwork, not a model architecture or performance chart.

To regenerate the hero, project illustration, and footer:

```sh
python3 scripts/build_artwork.py
```

The hero has a single 4.5-second motion sequence and respects reduced-motion preferences.
The README uses a separate mobile composition below 600px. The activity graphic has
light, dark, desktop, and mobile versions. All images also have text alternatives.

## Activity updates

The `Refresh profile activity` workflow runs weekly and can be run manually from Actions.
It uses GitHub's built-in token, with repository contents permission to commit SVG updates.
No personal access token or other secret needs to be added.

To regenerate locally with an authenticated GitHub CLI:

```sh
python3 scripts/update_activity.py
```

The year total comes from GitHub's contribution calendar. Mobile displays the last
26 weeks but labels the annual total explicitly. These are contribution counts,
not commit counts or a measure of all work. Data errors leave the existing artwork
intact; the date printed on it shows the last successful refresh.

GitHub can disable scheduled workflows in inactive public repositories. If the date
stops updating, check the Actions page and re-enable/run the workflow as needed.

## Profile finishing touches

Suggested account bio (separate from this README):

> AI engineer building agents, real-time vision, and learning systems. Founding engineer at AROH · Founding team at Lythe · Co-founder, NeuroNex Labs.

Suggested pinned repositories: Creating-AutoGrad-from-scratch, OpenOrbit, holo-vex,
and FacPosCheck. Pinning and the account bio are managed separately in GitHub's profile UI.

## Inspiration and platform references

- [GitHub profile README topic](https://github.com/topics/profile-readme)
- [Awesome GitHub Profile READMEs](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
- [GitHub: managing your profile README](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)

The layout and illustrations here are original; no showcase profile was copied.
