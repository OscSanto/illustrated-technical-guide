# Three-way visual experiment

Open `index.html` to view **paired** diagram candidates: AntV Infographic from declarative DSL (needs network/pinned JavaScript), and custom offline SVG figures. If the external renderer cannot load, the page reports that status and exposes the full DSL. It does not fake AntV output.

The `assets/` folder contains three `.infographic` source files and three SVG and PNG original figures. `figure_data.json` holds the exact input values and numeric outputs; `TEST_RESULTS.json` records local checks. Source diagram builder is `../../scripts/build_visual_comparison.py`.

Run `python ../../scripts/test_visual_comparison.py` from this folder to verify the examples.

**Offline:** open the `.svg` and `.png` files or view the right-side panels in `index.html`. **Online AntV experiment:** the left-side panels load `@antv/infographic@0.2.20` from a pinned CDN; export to static SVG before publication. The package itself is not bundled here, so the left panels require the CDN unless you replace it with a locally installed build.
