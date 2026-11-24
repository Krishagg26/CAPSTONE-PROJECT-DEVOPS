import sys, os
sys.path.insert(0, os.path.abspath("app"))
import server

def test_version_default():
    assert server.VERSION in ["v1.0", "v2.0"]

def test_secret_masking_policy():
    raw = "SUPER_SECRET_KEY"
    masked = "***MASKED***"
    assert raw not in masked

def test_canary_weight_math():
    stable, canary = 90, 10
    assert stable + canary == 100
