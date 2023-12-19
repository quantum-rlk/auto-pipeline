import pytest
from store_mgr import S3Mgr 

BUCKET='oblitrium'

g_s3=S3Mgr(BUCKET)

def test_push():
    g_key = g_s3.push('network.jpg') 
    assert g_key

def test_remove():
    assert g_s3.count() == 1
    for ielement in g_s3.list():
        g_s3.remove(ielement)
    assert g_s3.count() == 0 
