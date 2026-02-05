# U.S. Airbnb Analysis - README

Project overview
- Exploratory data analysis and visualizations for Airbnb listings (2020 & 2023 US snapshots).
- Tasks include: data loading, summary stats, missingness, correlations, outlier removal, KDE distributions, geographic visualizations (map + choropleth), city/state aggregations, and basic comparisons between 2020 and 2023.

Datasets required
- `AB_US_2020.csv` (used as `air2020`)
- `AB_US_2023.csv` (used as `air2023`)

Required packages
- Python 3.7+
- pandas, numpy
- matplotlib, seaborn
- plotly, plotly.express
- scikit-learn (sklearn)
- folium (if interactive leaflet maps are used)
- (Optional) jupyter notebook / jupyterlab

How to run
1. Open the provided Jupyter notebook.
2. Make sure the two CSV files are in the notebook working directory.
3. Run cells sequentially from top to bottom (the notebook relies on variables created by earlier cells).
4. If you add or reorder cells, ensure imports and variable definitions remain accessible for downstream cells.



Notes, pitfalls & quick fixes
- Cell 10 overwrites the 'skew' row with kurtosis due to using the same index twice. To add both skew and kurtosis use distinct row labels, e.g.:
    - desc.loc['skew'] = pr_data.skew()
    - desc.loc['kurtosis'] = pr_data.kurtosis()
- pandas.DataFrame.between(..., inclusive=...) behavior differs by pandas version. If you hit a deprecation error, replace with explicit comparisons: (price >= q_lower) & (price <= q_upper).
- Some mapping in `states_dic` is manual and incomplete; missing or mismapped city names will cause KeyError when applying the lambda. Use `states_dic.get(x, 'Unknown')` or filter for cities in the dictionary.
- Large datasets and interactive Plotly/folium maps can be slow. Consider sampling `pr_data` for quick exploration.
- Ensure plotly and folium are installed if you run interactive cells. In headless environments, use `plotly.io.renderers.default = 'notebook'` or save static images.

Suggestions for extension
- Build a reproducible preprocessing function for outlier removal and feature engineering.
- Train and evaluate regression models (Ridge, Lasso, RandomForest, etc.) on engineered features to predict price (some model objects appear created in the notebook).
- Add cross-validation and hyperparameter tuning with GridSearchCV (already partially prepared in notebook variables).

License & contact
- This README is a concise guide to run and understand each cell. For questions or improvements, update the notebook comments or add new cells explaining changes.# AirbnbAnalysis
