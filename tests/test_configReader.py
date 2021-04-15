from executorCommon.ConfigReader import MPCConfig


def test_readconfig():
    config = MPCConfig.from_json("Res/config0.json")
    assert config.self_id == "abc"
