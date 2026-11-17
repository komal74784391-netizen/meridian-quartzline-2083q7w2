from quartzline.pipeline import Pipeline


def test_pipeline_adds_feature():
    pipeline = Pipeline().add("double", lambda row: row["x"] * 2)
    rows = pipeline.run([{"x": 2}])
    assert rows[0]["double"] == 4
