import pandera as pa


class PredictSchema(pa.SchemaModel):
    radius_mean: pa.typing.Series[float]
    texture_mean: pa.typing.Series[float]
    perimeter_mean: pa.typing.Series[float]
    area_mean: pa.typing.Series[float]
    smoothness_mean: pa.typing.Series[float]
    compactness_mean: pa.typing.Series[float]
    concavity_mean: pa.typing.Series[float]
    concave_points_mean: pa.typing.Series[float]
    symmetry_mean: pa.typing.Series[float]
    fractal_dimension_mean: pa.typing.Series[float]
    radius_se: pa.typing.Series[float]
    texture_se: pa.typing.Series[float]
    perimeter_se: pa.typing.Series[float]
    area_se: pa.typing.Series[float]
    smoothness_se: pa.typing.Series[float]
    compactness_se: pa.typing.Series[float]
    concavity_se: pa.typing.Series[float]
    concave_points_se: pa.typing.Series[float]
    symmetry_se: pa.typing.Series[float]
    fractal_dimension_se: pa.typing.Series[float]
    radius_worst: pa.typing.Series[float]
    texture_worst: pa.typing.Series[float]
    perimeter_worst: pa.typing.Series[float]
    area_worst: pa.typing.Series[float]
    smoothness_worst: pa.typing.Series[float]
    compactness_worst: pa.typing.Series[float]
    concavity_worst: pa.typing.Series[float]
    concave_points_worst: pa.typing.Series[float]
    symmetry_worst: pa.typing.Series[float]
    fractal_dimension_worst: pa.typing.Series[float]

    class Config:
        coerce = True
