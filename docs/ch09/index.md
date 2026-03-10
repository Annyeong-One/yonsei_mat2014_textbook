# Chapter 9: Matplotlib


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

This chapter covers Matplotlib, the core plotting library in Python, including figure and axes objects, plot types (line, scatter, bar, histogram, heatmap, 3D), customization, layout management, and OOP design.

## 9.1 Introduction

- [Visualization Libraries](intro/visualization_libraries.md)
- [Python Data Science Ecosystem](intro/data_science_ecosystem.md)
- [Three Ways of Drawing](intro/three_ways_drawing.md)
- [Five Major Objects](intro/five_major_objects.md)
- [Interactive Mode](intro/interactive_mode.md)

## 9.2 Getting Started

- [Installation and Import](setup/installation.md)
- [OOP vs Pyplot Style](fundamentals/matplotlib_oop_vs_pyplot.md)
- [plt.subplot vs plt.subplots](setup/subplot_vs_subplots.md)
- [Style Sheets](setup/style_sheets.md)

## 9.3 Figure Object

- [Creating Figures](figure/creating_figures.md)
- [Figure Styles](figure/figure_styles.md)
- [Figure Methods](figure/figure_methods.md)
- [Saving Figures](figure/saving_figures.md)

## 9.4 Axes Object

- [Axes Basics](axes/axes_basics.md)
- [Creating Axes](axes/creating_axes.md)
- [Axes Shape Behavior](axes/axes_shape.md)
- [Unpacking Axes](axes/unpacking_axes.md)
- [add_subplot vs subplots](axes/add_subplot_vs_subplots.md)

## 9.5 Layout

- [Subplots and Grids](layout/subplots.md)
- [GridSpec](layout/gridspec.md)
- [subplot_mosaic](layout/subplot_mosaic.md)
- [Tight Layout](layout/tight_layout.md)

## 9.6 Line Plot

- [Basic Line Plot](line_plot/basic_line_plot.md)
- [Data Input Types](line_plot/data_input_types.md)
- [Line Styles and Colors](line_plot/line_styles_colors.md)
- [Markers](line_plot/markers.md)
- [Labels and Legends](line_plot/labels_legends.md)
- [Error Bars](line_plot/errorbar.md)

## 9.7 Axes Customization

- [Title and Labels](customization/title_labels.md)
- [Limits and Ticks](customization/limits_ticks.md)
- [Tick Labels](customization/tick_labels.md)
- [Grid and Axis](customization/grid_axis.md)
- [Logarithmic Scales](customization/log_scales.md)

## 9.8 Spine and Axis

- [Spine Customization](spine_axis/spine_customization.md)
- [Tick Control](spine_axis/tick_control.md)

## 9.9 Text and Annotations

- [Text Object](text/text_object.md)
- [Adding Text](text/adding_text.md)
- [Annotations](text/annotations.md)
- [LaTeX Support](text/latex_support.md)

## 9.10 Axes Enhancements

- [Twin Axes](advanced/twin_axes.md)
- [Secondary Axes](advanced/secondary_axes.md)
- [Fill and Fill Between](advanced/fill_between.md)
- [Axhline and Axvline](advanced/axhline_axvline.md)
- [Animation (FuncAnimation)](advanced/animation.md)
- [Polar Plots](advanced/polar_plots.md)
- [Quiver Plots](advanced/quiver_plots.md)

## 9.11 Histogram

- [Basic Histogram](histogram/basic_histogram.md)
- [Histogram Keywords](histogram/histogram_keywords.md)
- [Return Values](histogram/return_values.md)
- [Distribution Fitting](histogram/distribution_fitting.md)

## 9.12 Box Plot

- [Basic Box Plot](box_plot/basic_box_plot.md)
- [Box Plot Anatomy](box_plot/box_plot_anatomy.md)
- [Box Plot Keywords](box_plot/box_plot_keywords.md)
- [Styling and Colors](box_plot/styling_colors.md)
- [Violin Plot](box_plot/violin_plot.md)
- [Combined Visualizations](box_plot/combined_visualizations.md)

## 9.13 Scatter Plot

- [Basic Scatter Plot](scatter_plot/basic_scatter_plot.md)
- [Scatter Plot Keywords](scatter_plot/scatter_plot_keywords.md)
- [Color Mapping](scatter_plot/color_mapping.md)

## 9.14 Bar Chart

- [Basic Bar Chart](bar_chart/basic_bar_chart.md)
- [Bar Chart Keywords](bar_chart/bar_chart_keywords.md)
- [Grouped and Stacked](bar_chart/grouped_stacked.md)

## 9.15 Pie Chart

- [Basic Pie Chart](pie_chart/basic_pie_chart.md)
- [Pie Chart Keywords](pie_chart/pie_chart_keywords.md)
- [Customization Examples](pie_chart/customization.md)

## 9.16 Heatmap and Colormaps

- [Heatmaps with imshow](heatmap/imshow_heatmap.md)
- [Heatmaps with pcolormesh](heatmap/pcolormesh_heatmap.md)
- [Colormap Selection](heatmap/colormap_selection.md)
- [Colorbars](heatmap/colorbars.md)

## 9.17 2D Density Plots

- [Axes Method - hist2d](density_2d/hist2d.md)
- [Axes Method - hexbin](density_2d/hexbin.md)
- [Kernel Density Estimation](density_2d/kde_imshow.md)

## 9.18 Image Plot

- [Image I/O](image/image_io.md)
- [Image Processing](image/processing.md)
- [Applications](image/applications.md)

## 9.19 Contour Plot

- [Axes Method - contour](contour_plot/contour.md)
- [Axes Method - contourf](contour_plot/contourf.md)
- [Axes Method - clabel](contour_plot/clabel.md)
- [Contour and Surface](contour_plot/contour_surface.md)

## 9.20 3D Plot

- [Creating 3D Axes](3d_plot/creating_3d_axes.md)
- [Axes Method - plot (3D Lines)](3d_plot/plot_3d.md)
- [Axes Method - plot_surface](3d_plot/plot_surface.md)
- [Axes Method - view_init](3d_plot/view_init.md)
- [Complex Function Visualization](3d_plot/complex_functions.md)

## 9.21 Practical Examples

- [Financial Charts](examples/financial_charts.md)
- [Brownian Motion](examples/brownian_motion.md)
- [Mathematical Functions](examples/math_functions.md)
- [Statistical Distributions](examples/statistical_distributions.md)

## 9.22 Matplotlib OOP Design

- [Matplotlib Hierarchy](oop/matplotlib_hierarchy.md)
- [Matplotlib Artists](oop/matplotlib_artists.md)
