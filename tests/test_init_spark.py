from tests.context import sc


def test_spark_context():
    rdd = sc.parallelize([1, 2, 3])
    assert rdd.count() == 3
