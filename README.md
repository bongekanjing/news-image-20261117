# Tuesday 17 November 2026 — The World in One Day

[![news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![Rank](https://make.fun/badge/news-image-20261117/bongekanjing/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![Reward](https://make.fun/badge/news-image-20261117/bongekanjing/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

Entry for the [make.fun news-image-20261117 bounty](https://make.fun/bounty/news-image-20261117): one image summing up the world news of Tuesday 17 November 2026.

The image is drawn programmatically with PIL — a date banner plus six panels, one per story:

1. **Ukraine hits the Crimea bridge again** — a second strike in under 24 hours collapses part of the Kerch road bridge; Russia answers with ballistic missiles on Kyiv's Dnipro bridges.
2. **Tankers struck by mines near Hormuz** — two oil tankers catch fire after hitting mines south of the Strait of Hormuz; Iran fires drones at a US radar base in Bahrain as a third US carrier reaches the region.
3. **Trump, Xi and Putin to meet in Shenzhen** — China confirms the first three-way summit of the three leaders, set for Thursday on the sidelines of the APEC meeting.
4. **Five nations plan a Rwanda return hub** — Germany, Denmark, Austria, Greece and the Netherlands unveil a joint facility in Rwanda for rejected asylum seekers.
5. **Pentagon fails its audit — ninth year** — auditors again cannot verify accounts covering more than $4.8 trillion in assets.
6. **UN: 1,390 civilians killed in Sudan** — a UN report counts at least 1,390 civilians killed in Sudan's conflict in the first half of 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024×1024 PNG, < 1 MiB)
```

`main.py` (Python 3.13, standard library only, no network) copies the pre-drawn `entry.png` to the output directory. Running it twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
